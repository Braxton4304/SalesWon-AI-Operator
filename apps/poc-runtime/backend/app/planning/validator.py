# implements: runtime-spec, governance-spec

"""Validate ActionPlan against policy, data-spec, and agent authority."""

from __future__ import annotations

from dataclasses import dataclass

from app.agent.manifest import load_manifest
from app.intent.schemas import Intent
from app.planning.schema import ActionPlan
from app.security.user_context import CurrentUserContext


class PlanValidationError(Exception):
    def __init__(self, status: str, message: str = "") -> None:
        self.status = status
        self.message = message
        super().__init__(message or status)


@dataclass
class ValidationResult:
    plan: ActionPlan
    intent: Intent


SUPPORTED_INTENTS = {
    Intent.SEARCH_OPPORTUNITIES,
    Intent.SEARCH_ACTIVITIES,
    Intent.SEARCH_ACCOUNTS,
    Intent.GET_RECORD,
    Intent.UPDATE_ACTIVITY,
}

WRITE_INTENTS = {Intent.UPDATE_ACTIVITY}


class PlanValidator:
    def validate(self, plan: ActionPlan, ctx: CurrentUserContext) -> ValidationResult:
        _ = ctx
        manifest = load_manifest()

        if plan.primary_agent not in manifest.agent_ids():
            raise PlanValidationError("unsupported_action", f"Unknown agent: {plan.primary_agent}")

        intent = plan.to_intent()
        if intent == Intent.UNKNOWN:
            raise PlanValidationError("unsupported_action", "Unknown or unsupported intent")

        if intent not in SUPPORTED_INTENTS:
            raise PlanValidationError("unsupported_action", f"Intent not supported: {intent.value}")

        if intent not in WRITE_INTENTS and plan.proposed_patch:
            raise PlanValidationError("unsafe_write", "Read intents cannot include proposed_patch")

        if intent == Intent.UPDATE_ACTIVITY:
            if plan.proposed_patch is None and not plan.missing_fields:
                raise PlanValidationError("unsafe_write", "update_activity requires proposed_patch or missing_fields")

        if intent != Intent.UPDATE_ACTIVITY and plan.requires_confirmation:
            raise PlanValidationError("unsupported_action", "Only writes require confirmation")

        return ValidationResult(plan=plan, intent=intent)
