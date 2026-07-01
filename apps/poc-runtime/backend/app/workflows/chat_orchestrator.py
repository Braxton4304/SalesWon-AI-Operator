# implements: runtime-spec, data-spec, governance-spec

"""Main chat orchestration — compile → plan → validate → execute → narrate."""

from __future__ import annotations

from typing import Any

from app.audit.logger import get_audit_logger
from app.audit.schema import AuditOutcome, AuditRecord, DecisionAction
from app.connectors.saleswon.base import SalesWonConnector
from app.connectors.saleswon.servicenow import ServiceNowSalesWonConnector
from app.intent.schemas import Intent
from app.llm.factory import get_llm_provider
from app.llm.base import LLMProvider
from app.memory.short_term import SessionState, ShortTermMemory, get_short_term_memory
from app.planning.executor import PlanExecutor
from app.planning.results import PlanExecutionResult
from app.planning.schema import ActionPlan
from app.planning.validator import PlanValidationError, PlanValidator
from app.runtime.clarification import get_clarification_store
from app.runtime.decision_engine import DecisionEngine, DecisionResult
from app.runtime.prompt_compiler import CompiledPrompt, PromptCompiler
from app.security.user_context import CurrentUserContext, ScopeDenied
from app.workflows.activity_update import ActivityUpdateWorkflow, WorkflowResponse


class ChatOrchestrator:
    def __init__(
        self,
        connector: SalesWonConnector | None = None,
        llm: LLMProvider | None = None,
        memory: ShortTermMemory | None = None,
    ) -> None:
        self._connector = connector or ServiceNowSalesWonConnector()
        self._llm = llm or get_llm_provider()
        self._memory = memory or get_short_term_memory()
        self._compiler = PromptCompiler()
        self._validator = PlanValidator()
        self._scope_engine = DecisionEngine()
        self._audit = get_audit_logger()
        self._activity_workflow = ActivityUpdateWorkflow(
            connector=self._connector,
            llm=self._llm,
            engine=self._scope_engine,
        )
        self._executor = PlanExecutor(
            connector=self._connector,
            engine=self._scope_engine,
            activity_workflow=self._activity_workflow,
        )

    def handle_message(
        self,
        ctx: CurrentUserContext,
        message: str,
        session_id: str | None = None,
    ) -> WorkflowResponse:
        session = self._memory.get_or_create(session_id)

        pending_context: dict[str, Any] | None = None
        if session.pending_intent:
            pending_context = {
                "intent": session.pending_intent,
                "fields": session.pending_fields,
                "primary_agent": session.pending_primary_agent or "sales-rep",
            }
            session.pending_intent = None
            session.pending_fields = {}
            session.pending_primary_agent = None

        compiled = self._compiler.compile(ctx, session, message, pending_context)
        self._memory.add_turn(session, "user", message)

        plan = self._llm.plan(compiled)

        try:
            validation = self._validator.validate(plan, ctx)
        except PlanValidationError as exc:
            decision = (
                self._scope_engine.decide_refuse(exc.status, plan.confidence)
                if exc.status
                in {"scope_denied", "unsupported_action", "unsafe_write", "missing_authority"}
                else self._scope_engine.decide_unsupported(plan.confidence)
            )
            execution = PlanExecutionResult(
                decision=decision,
                intent=plan.to_intent(),
                primary_agent=plan.primary_agent,
            )
            return self._build_response(
                ctx, session, plan, compiled, execution, f"validation failed: {exc.status}"
            )

        execution = self._executor.execute(validation, ctx, session)
        return self._build_response(
            ctx,
            session,
            plan,
            compiled,
            execution,
            request_summary=f"plan: {plan.intent}",
            skip_audit=execution.audit_id is not None,
        )

    def handle_confirm(
        self,
        ctx: CurrentUserContext,
        pending_confirmation_id: str,
        session_id: str | None = None,
    ) -> WorkflowResponse:
        store = get_clarification_store()
        pending = store.pop(pending_confirmation_id)
        if not pending:
            decision = DecisionResult(
                decision_action=DecisionAction.REFUSE,
                confidence_score=1.0,
                status="unsupported_action",
            )
            session = self._memory.get_or_create(session_id)
            plan = ActionPlan(intent=Intent.UPDATE_ACTIVITY.value)
            compiled = self._stub_compiled(ctx, session)
            execution = PlanExecutionResult(
                decision=decision, intent=Intent.UPDATE_ACTIVITY
            )
            return self._build_response(
                ctx, session, plan, compiled, execution, "expired confirmation"
            )

        if pending.actor != ctx.user_id or pending.tenant_id != ctx.tenant_id:
            decision = DecisionEngine.from_scope_denied(ScopeDenied("scope_denied"))
            session = self._memory.get_or_create(session_id)
            plan = ActionPlan(intent=Intent.UPDATE_ACTIVITY.value)
            compiled = self._stub_compiled(ctx, session)
            execution = PlanExecutionResult(
                decision=decision, intent=Intent.UPDATE_ACTIVITY
            )
            return self._build_response(
                ctx, session, plan, compiled, execution, "confirmation scope denied"
            )

        session = self._memory.get_or_create(session_id or pending.session_id)
        response = self._activity_workflow.execute_confirmed(ctx, session, pending)
        self._memory.add_turn(session, "assistant", response.response_payload)
        return response

    def _build_response(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        plan: ActionPlan,
        compiled: CompiledPrompt,
        execution: PlanExecutionResult,
        request_summary: str,
        skip_audit: bool = False,
    ) -> WorkflowResponse:
        decision = execution.decision
        narrative = execution.response_payload or self._llm.generate_response(
            plan, execution, compiled
        )

        audit_id = execution.audit_id
        if not skip_audit:
            outcome = AuditOutcome.SUCCESS
            if decision.decision_action == DecisionAction.REFUSE:
                outcome = AuditOutcome.REFUSED
            elif decision.decision_action == DecisionAction.ESCALATE:
                outcome = AuditOutcome.ESCALATED
            elif decision.status == "connector_pending_credentials":
                outcome = AuditOutcome.PENDING
            elif decision.decision_action == DecisionAction.RECOMMEND:
                outcome = AuditOutcome.PENDING
            elif decision.decision_action == DecisionAction.ASK:
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
                intent=execution.intent.value,
                filters=plan.filters,
                proposed_action=execution.proposed_action,
            )
            self._audit.write(record)
            audit_id = record.correlation_id

        self._memory.add_turn(session, "assistant", narrative)

        return WorkflowResponse(
            response_payload=narrative,
            decision_action=decision.decision_action,
            confidence_score=decision.confidence_score,
            source_references=decision.source_references or [],
            audit_id=audit_id or "",
            session_id=session.session_id,
            status=decision.status,
            pending_confirmation_id=execution.pending_confirmation_id,
            proposed_action=execution.proposed_action,
            primary_agent=plan.primary_agent,
        )

    @staticmethod
    def _stub_compiled(ctx: CurrentUserContext, session: SessionState) -> CompiledPrompt:
        return CompiledPrompt(
            system_message="",
            developer_message="",
            messages=[],
            user_context=ctx,
            session_id=session.session_id,
            current_request="",
            primary_agent="sales-rep",
        )


_orchestrator: ChatOrchestrator | None = None


def get_chat_orchestrator() -> ChatOrchestrator:
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = ChatOrchestrator()
    return _orchestrator
