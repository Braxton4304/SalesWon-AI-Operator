# implements: runtime-spec, data-spec, governance-spec

"""Execute validated ActionPlan via connector — LLM never writes directly."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from app.connectors.saleswon.base import ConnectorNotConfigured, SalesWonConnector
from app.intent.schemas import Intent
from app.memory.short_term import SessionState
from app.planning.results import PlanExecutionResult
from app.planning.schema import ActionPlan
from app.planning.validator import ValidationResult
from app.runtime.clarification import ClarificationStore, get_clarification_store
from app.runtime.decision_engine import DecisionEngine, DecisionResult
from app.security.user_context import CurrentUserContext, ScopeDenied, ScopeEnforcer

if TYPE_CHECKING:
    from app.workflows.activity_update import ActivityUpdateWorkflow


class PlanExecutor:
    def __init__(
        self,
        connector: SalesWonConnector,
        scope: ScopeEnforcer | None = None,
        engine: DecisionEngine | None = None,
        clarification: ClarificationStore | None = None,
        activity_workflow: ActivityUpdateWorkflow | None = None,
    ) -> None:
        self._connector = connector
        self._scope = scope or ScopeEnforcer()
        self._engine = engine or DecisionEngine()
        self._clarification = clarification or get_clarification_store()
        self._activity = activity_workflow

    def execute(
        self,
        validation: ValidationResult,
        ctx: CurrentUserContext,
        session: SessionState,
    ) -> PlanExecutionResult:
        plan = validation.plan
        intent = validation.intent
        confidence = plan.confidence or 0.75

        if plan.missing_fields:
            question = plan.clarifying_question or (
                f"I need: {', '.join(plan.missing_fields)}"
            )
            session.pending_intent = intent.value
            session.pending_fields = plan.plan_fields_for_executor()
            session.pending_primary_agent = plan.primary_agent
            decision = self._engine.decide_ask(plan.missing_fields, confidence)
            decision.context = {
                **(decision.context or {}),
                "missing_fields": plan.missing_fields,
                "clarifying_question": question,
            }
            return PlanExecutionResult(
                decision=decision,
                intent=intent,
                primary_agent=plan.primary_agent,
            )

        if intent == Intent.UPDATE_ACTIVITY:
            return self._execute_update(plan, ctx, session, confidence)

        return self._execute_read(plan, intent, ctx, confidence)

    def _execute_read(
        self,
        plan: ActionPlan,
        intent: Intent,
        ctx: CurrentUserContext,
        confidence: float,
    ) -> PlanExecutionResult:
        fields = plan.plan_fields_for_executor()
        scoped = self._scope.apply_read_filters(ctx, {**plan.filters, **fields})

        try:
            records = self._execute_connector_read(ctx, intent, scoped, fields, plan.object_type)
            decision = self._engine.decide_read(intent, confidence, records)
            return PlanExecutionResult(
                decision=decision,
                intent=intent,
                records=records,
                primary_agent=plan.primary_agent,
            )
        except ConnectorNotConfigured as exc:
            decision = self._engine.decide_read(intent, confidence, connector_error=exc)
            return PlanExecutionResult(decision=decision, intent=intent, primary_agent=plan.primary_agent)
        except ScopeDenied as exc:
            decision = DecisionEngine.from_scope_denied(exc)
            return PlanExecutionResult(decision=decision, intent=intent, primary_agent=plan.primary_agent)

    def _execute_connector_read(
        self,
        ctx: CurrentUserContext,
        intent: Intent,
        filters: dict[str, Any],
        fields: dict[str, Any],
        object_type: str | None,
    ) -> list[Any]:
        if intent == Intent.SEARCH_OPPORTUNITIES:
            return self._connector.search_opportunities(ctx, filters)
        if intent == Intent.SEARCH_ACTIVITIES:
            return self._connector.search_activities(ctx, filters)
        if intent == Intent.SEARCH_ACCOUNTS:
            return self._connector.search_accounts(ctx, filters)
        if intent == Intent.GET_RECORD:
            sys_id = fields.get("sys_id") or filters.get("sys_id")
            if not sys_id:
                raise ScopeDenied("unsupported_action")
            obj = object_type or "activity"
            record = self._connector.get_record(ctx, obj, sys_id)
            self._scope.assert_record_visible(ctx, record.__dict__)
            return [record]
        return []

    def _execute_update(
        self,
        plan: ActionPlan,
        ctx: CurrentUserContext,
        session: SessionState,
        confidence: float,
    ) -> PlanExecutionResult:
        if self._activity is None:
            raise RuntimeError("ActivityUpdateWorkflow required for update_activity")

        fields = plan.plan_fields_for_executor()
        if plan.filters.get("account_name") and "account_name" not in fields:
            fields["account_name"] = plan.filters["account_name"]
        if plan.proposed_patch:
            if "status" in plan.proposed_patch:
                fields["status"] = plan.proposed_patch["status"]
            if "due_date" in plan.proposed_patch:
                fields["due_date"] = plan.proposed_patch["due_date"]
            fields.setdefault("sys_id", plan.filters.get("sys_id"))

        if plan.requires_confirmation or plan.proposed_patch:
            wf = self._activity.prepare_update(ctx, session, fields, confidence)
            return PlanExecutionResult(
                decision=DecisionResult(
                    decision_action=wf.decision_action,
                    confidence_score=wf.confidence_score,
                    status=wf.status,
                    source_references=wf.source_references,
                    context={"proposed_action": wf.proposed_action},
                ),
                intent=Intent.UPDATE_ACTIVITY,
                proposed_action=wf.proposed_action,
                pending_confirmation_id=wf.pending_confirmation_id,
                primary_agent=plan.primary_agent,
                response_payload=wf.response_payload,
                audit_id=wf.audit_id,
            )

        decision = self._engine.decide_ask(["proposed_patch"], confidence)
        return PlanExecutionResult(
            decision=decision,
            intent=Intent.UPDATE_ACTIVITY,
            primary_agent=plan.primary_agent,
        )
