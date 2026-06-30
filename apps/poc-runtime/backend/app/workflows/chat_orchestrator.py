# implements: runtime-spec, data-spec, governance-spec

"""Main chat orchestration service."""

from __future__ import annotations

from typing import Any

from app.audit.logger import get_audit_logger
from app.audit.schema import AuditOutcome, AuditRecord, DecisionAction
from app.connectors.saleswon.base import ConnectorNotConfigured, SalesWonConnector
from app.connectors.saleswon.servicenow import ServiceNowSalesWonConnector
from app.intent.router import IntentRouter
from app.intent.schemas import Intent
from app.llm.factory import get_llm_provider
from app.llm.base import LLMProvider
from app.memory.short_term import SessionState, ShortTermMemory, get_short_term_memory
from app.runtime.context_assembly import assemble_context
from app.runtime.decision_engine import DecisionEngine, DecisionResult
from app.security.user_context import CurrentUserContext, ScopeDenied, ScopeEnforcer
from app.workflows.activity_update import ActivityUpdateWorkflow, WorkflowResponse


class ChatOrchestrator:
    SUPPORTED_INTENTS = {
        Intent.SEARCH_OPPORTUNITIES,
        Intent.SEARCH_ACTIVITIES,
        Intent.SEARCH_ACCOUNTS,
        Intent.GET_RECORD,
        Intent.UPDATE_ACTIVITY,
    }

    def __init__(
        self,
        connector: SalesWonConnector | None = None,
        llm: LLMProvider | None = None,
        memory: ShortTermMemory | None = None,
    ) -> None:
        self._connector = connector or ServiceNowSalesWonConnector()
        self._llm = llm or get_llm_provider()
        self._memory = memory or get_short_term_memory()
        self._router = IntentRouter(self._llm)
        self._scope = ScopeEnforcer()
        self._engine = DecisionEngine()
        self._audit = get_audit_logger()
        self._activity_workflow = ActivityUpdateWorkflow(
            connector=self._connector,
            llm=self._llm,
            scope=self._scope,
            engine=self._engine,
        )

    def handle_message(
        self,
        ctx: CurrentUserContext,
        message: str,
        session_id: str | None = None,
    ) -> WorkflowResponse:
        session = self._memory.get_or_create(session_id)
        history = self._memory.get_history(session)

        if session.pending_intent == Intent.UPDATE_ACTIVITY.value:
            routed = self._router.route(message, history)
            merged = IntentRouter.merge_fields(session.pending_fields, routed.extraction.fields)
            session.pending_intent = None
            session.pending_fields = {}
            self._memory.add_turn(session, "user", message)
            response = self._activity_workflow.prepare_update(
                ctx, session, merged, routed.classification.confidence
            )
            response.session_id = session.session_id
            self._memory.add_turn(session, "assistant", response.response_payload)
            return response

        routed = self._router.route(message, history)
        intent = routed.classification.intent
        confidence = routed.classification.confidence
        fields = routed.extraction.fields

        assemble_context(ctx, message, history)

        if intent == Intent.UNKNOWN:
            decision = self._engine.decide_unsupported(confidence)
            return self._respond(ctx, session, message, intent, decision, "unsupported intent")

        if intent not in self.SUPPORTED_INTENTS:
            decision = self._engine.decide_unsupported(confidence)
            return self._respond(ctx, session, message, intent, decision, "unsupported intent")

        if intent == Intent.UPDATE_ACTIVITY:
            self._memory.add_turn(session, "user", message)
            response = self._activity_workflow.prepare_update(
                ctx, session, fields, confidence
            )
            response.session_id = session.session_id
            self._memory.add_turn(session, "assistant", response.response_payload)
            return response

        if intent == Intent.GET_RECORD and not fields.get("sys_id"):
            if routed.extraction.missing_required or not fields.get("sys_id"):
                decision = self._engine.decide_ask(["sys_id"], confidence)
                return self._respond(
                    ctx, session, message, intent, decision, "get_record — missing sys_id"
                )

        return self._handle_read(ctx, session, message, intent, confidence, fields)

    def handle_confirm(
        self,
        ctx: CurrentUserContext,
        pending_confirmation_id: str,
        session_id: str | None = None,
    ) -> WorkflowResponse:
        from app.runtime.clarification import get_clarification_store

        store = get_clarification_store()
        pending = store.pop(pending_confirmation_id)
        if not pending:
            decision = DecisionResult(
                decision_action=DecisionAction.REFUSE,
                confidence_score=1.0,
                status="unsupported_action",
            )
            session = self._memory.get_or_create(session_id)
            return self._respond(
                ctx,
                session,
                "confirm",
                Intent.UPDATE_ACTIVITY,
                decision,
                "expired or invalid confirmation",
            )

        if pending.actor != ctx.user_id or pending.tenant_id != ctx.tenant_id:
            decision = DecisionEngine.from_scope_denied(ScopeDenied("scope_denied"))
            session = self._memory.get_or_create(session_id)
            return self._respond(
                ctx,
                session,
                "confirm",
                Intent.UPDATE_ACTIVITY,
                decision,
                "confirmation scope denied",
            )

        session = self._memory.get_or_create(session_id or pending.session_id)
        response = self._activity_workflow.execute_confirmed(ctx, session, pending)
        self._memory.add_turn(session, "assistant", response.response_payload)
        return response

    def _handle_read(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        message: str,
        intent: Intent,
        confidence: float,
        fields: dict[str, Any],
    ) -> WorkflowResponse:
        self._memory.add_turn(session, "user", message)
        scoped_filters = self._scope.apply_read_filters(ctx, fields)

        try:
            records = self._execute_read(ctx, intent, scoped_filters, fields)
            decision = self._engine.decide_read(intent, confidence, records)
        except ConnectorNotConfigured as exc:
            decision = self._engine.decide_read(intent, confidence, connector_error=exc)
        except ScopeDenied as exc:
            decision = DecisionEngine.from_scope_denied(exc)

        return self._respond(ctx, session, message, intent, decision, f"read: {intent.value}")

    def _execute_read(
        self,
        ctx: CurrentUserContext,
        intent: Intent,
        filters: dict[str, Any],
        fields: dict[str, Any],
    ) -> list[Any]:
        if intent == Intent.SEARCH_OPPORTUNITIES:
            return self._connector.search_opportunities(ctx, filters)
        if intent == Intent.SEARCH_ACTIVITIES:
            return self._connector.search_activities(ctx, filters)
        if intent == Intent.SEARCH_ACCOUNTS:
            return self._connector.search_accounts(ctx, filters)
        if intent == Intent.GET_RECORD:
            sys_id = fields.get("sys_id")
            if not sys_id:
                raise ScopeDenied("unsupported_action")
            object_type = fields.get("object_type", "activity")
            record = self._connector.get_record(ctx, object_type, sys_id)
            self._scope.assert_record_visible(ctx, record.__dict__)
            return [record]
        return []

    def _respond(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        message: str,
        intent: Intent,
        decision: DecisionResult,
        request_summary: str,
    ) -> WorkflowResponse:
        context = decision.context or {}
        if decision.status:
            context["status"] = decision.status

        response_text = self._llm.generate_response(
            intent, decision.decision_action.value, context
        )

        outcome = AuditOutcome.SUCCESS
        if decision.decision_action == DecisionAction.REFUSE:
            outcome = AuditOutcome.REFUSED
        elif decision.decision_action == DecisionAction.ESCALATE:
            outcome = AuditOutcome.ESCALATED
        elif decision.status == "connector_pending_credentials":
            outcome = AuditOutcome.PENDING

        record = AuditRecord(
            tenant_id=ctx.tenant_id,
            actor=ctx.user_id,
            decision_action=decision.decision_action,
            confidence_score=decision.confidence_score,
            source_references=decision.source_references or [],
            outcome=outcome,
            request_summary=request_summary,
            status=decision.status,
            intent=intent.value,
            filters=context.get("filters"),
        )
        self._audit.write(record)
        self._memory.add_turn(session, "assistant", response_text)

        return WorkflowResponse(
            response_payload=response_text,
            decision_action=decision.decision_action,
            confidence_score=decision.confidence_score,
            source_references=decision.source_references or [],
            audit_id=record.correlation_id,
            session_id=session.session_id,
            status=decision.status,
        )


_orchestrator: ChatOrchestrator | None = None


def get_chat_orchestrator() -> ChatOrchestrator:
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = ChatOrchestrator()
    return _orchestrator
