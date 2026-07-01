# implements: runtime-spec, data-spec, governance-spec

"""Activity update workflow with clarification and confirmation gates."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.audit.logger import get_audit_logger
from app.audit.schema import AuditOutcome, AuditRecord, DecisionAction
from app.connectors.saleswon.base import ConnectorNotConfigured, SalesWonConnector
from app.intent.schemas import Intent
from app.llm.base import LLMProvider
from app.memory.short_term import SessionState
from app.runtime.clarification import ClarificationStore, PendingAction
from app.runtime.decision_engine import DecisionEngine, DecisionResult
from app.security.user_context import CurrentUserContext, ScopeDenied, ScopeEnforcer


@dataclass
class WorkflowResponse:
    response_payload: str
    decision_action: DecisionAction
    confidence_score: float
    source_references: list[str]
    audit_id: str
    session_id: str | None = None
    status: str | None = None
    pending_confirmation_id: str | None = None
    proposed_action: dict[str, Any] | None = None
    primary_agent: str | None = None


class ActivityUpdateWorkflow:
    REQUIRED_FIELDS = ["activity_identifier", "status"]

    def __init__(
        self,
        connector: SalesWonConnector,
        llm: LLMProvider,
        scope: ScopeEnforcer | None = None,
        engine: DecisionEngine | None = None,
        clarification: ClarificationStore | None = None,
    ) -> None:
        self._connector = connector
        self._llm = llm
        self._scope = scope or ScopeEnforcer()
        self._engine = engine or DecisionEngine()
        from app.runtime.clarification import get_clarification_store

        self._clarification = clarification or get_clarification_store()
        self._audit = get_audit_logger()

    def prepare_update(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        fields: dict[str, Any],
        confidence: float,
    ) -> WorkflowResponse:
        missing = [
            f
            for f in self.REQUIRED_FIELDS
            if f == "activity_identifier"
            and "sys_id" not in fields
            and "account_name" not in fields
            or f == "status"
            and "status" not in fields
        ]
        if missing:
            session.pending_intent = Intent.UPDATE_ACTIVITY.value
            session.pending_fields.update(fields)
            decision = self._engine.decide_ask(missing, confidence)
            return self._finalize(
                ctx=ctx,
                session=session,
                decision=decision,
                intent=Intent.UPDATE_ACTIVITY,
                request_summary="activity update — missing fields",
            )

        proposed = {
            "object_type": "activity",
            "sys_id": fields.get("sys_id"),
            "account_name": fields.get("account_name"),
            "patch": {"state": fields.get("status")},
        }

        if fields.get("sys_id"):
            try:
                record = self._connector.get_record(
                    ctx, "activity", fields["sys_id"]
                )
                self._scope.assert_update_allowed(ctx, record.__dict__)
            except ConnectorNotConfigured:
                # Connector not wired yet — proceed to recommend; scope verified on confirm.
                pass
            except ScopeDenied as exc:
                decision = DecisionEngine.from_scope_denied(exc)
                return self._finalize(
                    ctx=ctx,
                    session=session,
                    decision=decision,
                    intent=Intent.UPDATE_ACTIVITY,
                    request_summary="activity update — scope denied",
                )

        pending = self._clarification.create(
            session_id=session.session_id,
            intent=Intent.UPDATE_ACTIVITY.value,
            fields=fields,
            proposed_action=proposed,
            actor=ctx.user_id,
            tenant_id=ctx.tenant_id,
        )
        decision = self._engine.decide_recommend(proposed, confidence)
        response = self._finalize(
            ctx=ctx,
            session=session,
            decision=decision,
            intent=Intent.UPDATE_ACTIVITY,
            request_summary="activity update — awaiting confirmation",
            proposed_action=proposed,
            confirmation=False,
        )
        response.pending_confirmation_id = pending.pending_id
        return response

    def execute_confirmed(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        pending: PendingAction,
    ) -> WorkflowResponse:
        proposed = pending.proposed_action
        sys_id = proposed.get("sys_id") or pending.fields.get("sys_id")

        if not sys_id:
            decision = self._engine.decide_ask(
                ["sys_id — activity record identifier required for write"],
                0.70,
            )
            return self._finalize(
                ctx=ctx,
                session=session,
                decision=decision,
                intent=Intent.UPDATE_ACTIVITY,
                request_summary="activity update confirm — missing sys_id",
                confirmation=True,
            )

        try:
            record = self._connector.get_record(ctx, "activity", sys_id)
            self._scope.assert_update_allowed(ctx, record.__dict__)
            result = self._connector.update_activity(
                ctx, sys_id, proposed.get("patch", {})
            )
            decision = self._engine.decide_write_result(0.90, write_result=result)
            outcome = AuditOutcome.SUCCESS
        except ConnectorNotConfigured as exc:
            decision = self._engine.decide_write_result(0.90, connector_error=exc)
            outcome = AuditOutcome.PENDING
        except ScopeDenied as exc:
            decision = DecisionEngine.from_scope_denied(exc)
            outcome = AuditOutcome.REFUSED
        else:
            outcome = AuditOutcome.SUCCESS

        return self._finalize(
            ctx=ctx,
            session=session,
            decision=decision,
            intent=Intent.UPDATE_ACTIVITY,
            request_summary="activity update — confirmed",
            proposed_action=proposed,
            confirmation=True,
            outcome_override=outcome if decision.status == "connector_pending_credentials" else None,
        )

    def _finalize(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        decision: DecisionResult,
        intent: Intent,
        request_summary: str,
        proposed_action: dict[str, Any] | None = None,
        confirmation: bool | None = None,
        outcome_override: AuditOutcome | None = None,
    ) -> WorkflowResponse:
        context = decision.context or {}
        if proposed_action:
            context["proposed_action"] = proposed_action
        if decision.status:
            context["status"] = decision.status

        response_text = self._narrate(ctx, session, intent, decision, proposed_action)

        outcome = outcome_override or self._map_outcome(decision)
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
            proposed_action=proposed_action,
            confirmation=confirmation,
        )
        self._audit.write(record)

        return WorkflowResponse(
            response_payload=response_text,
            decision_action=decision.decision_action,
            confidence_score=decision.confidence_score,
            source_references=decision.source_references or [],
            audit_id=record.correlation_id,
            session_id=session.session_id,
            status=decision.status,
            proposed_action=proposed_action,
        )

    def _narrate(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        intent: Intent,
        decision: DecisionResult,
        proposed_action: dict[str, Any] | None,
    ) -> str:
        from app.planning.results import PlanExecutionResult
        from app.planning.schema import ActionPlan
        from app.runtime.prompt_compiler import CompiledPrompt

        plan = ActionPlan(intent=intent.value, confidence=decision.confidence_score)
        compiled = CompiledPrompt(
            system_message="",
            developer_message="",
            messages=[],
            user_context=ctx,
            session_id=session.session_id,
            current_request="",
            primary_agent="sales-rep",
        )
        execution = PlanExecutionResult(
            decision=decision,
            intent=intent,
            proposed_action=proposed_action,
        )
        return self._llm.generate_response(plan, execution, compiled)

    @staticmethod
    def _map_outcome(decision: DecisionResult) -> AuditOutcome:
        if decision.decision_action == DecisionAction.REFUSE:
            return AuditOutcome.REFUSED
        if decision.decision_action == DecisionAction.ESCALATE:
            return AuditOutcome.ESCALATED
        if decision.status == "connector_pending_credentials":
            return AuditOutcome.PENDING
        if decision.decision_action == DecisionAction.RECOMMEND:
            return AuditOutcome.PENDING
        return AuditOutcome.SUCCESS
