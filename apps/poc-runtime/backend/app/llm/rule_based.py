# implements: runtime-spec

"""Deterministic rule-based LLM fallback for offline dev and CI."""

from __future__ import annotations

import json
import re

from app.intent.schemas import Intent
from app.llm.base import LLMProvider
from app.planning.results import PlanExecutionResult
from app.planning.schema import ActionPlan
from app.runtime.prompt_compiler import CompiledPrompt
from app.agent.selector import select_primary_agent


class RuleBasedLLMProvider(LLMProvider):
    def plan(self, compiled: CompiledPrompt) -> ActionPlan:
        message = compiled.current_request.lower()
        primary = select_primary_agent(message=compiled.current_request)

        if re.search(r"\b(send email|delete|create opportunity|update opportunity|forecast)\b", message):
            return ActionPlan(
                primary_agent=primary,
                intent=Intent.UNKNOWN.value,
                confidence=0.95,
            )

        if re.search(r"\b(update|mark|complete|close|change|move)\b.*\b(activity|call|task|follow-up|follow up)\b", message) or (
            re.search(r"\b(mark|complete|move)\b", message) and "acme" in message
        ):
            account_match = re.search(r"\bacme\b", message, re.I)
            status_match = re.search(r"\b(done|complete|completed|closed)\b", message, re.I)
            due_match = re.search(r"\bfriday\b", message, re.I)
            patch: dict = {}
            missing: list[str] = []
            if status_match:
                patch["status"] = status_match.group(1).lower()
            if due_match:
                patch["due_date"] = "next_friday"
            if not patch:
                missing.append("status")
            filters = {"account_name": account_match.group(0) if account_match else "Acme"}
            if "sys_id" not in message and not account_match:
                missing.append("activity_identifier")
            return ActionPlan(
                primary_agent="follow-up" if "follow" in message else primary,
                intent=Intent.UPDATE_ACTIVITY.value,
                object_type="activity",
                filters=filters,
                proposed_patch=patch or None,
                missing_fields=missing,
                requires_confirmation=not missing,
                clarifying_question="Which activity should I update?" if missing else None,
                confidence=0.88 if not missing else 0.70,
            )

        if re.search(r"\b(opportunit(y|ies)|pipeline|deals?)\b", message) and "quarter" in message:
            return ActionPlan(
                primary_agent="sales-rep",
                intent=Intent.SEARCH_OPPORTUNITIES.value,
                object_type="opportunity",
                filters={"close_date_range": "this_quarter"},
                confidence=0.88,
                user_summary_hint="Summarize deals closing this quarter",
            )

        if re.search(r"\boverdue\b", message) and re.search(r"\bactivit", message):
            return ActionPlan(
                primary_agent="follow-up",
                intent=Intent.SEARCH_ACTIVITIES.value,
                object_type="activity",
                filters={"overdue": True},
                confidence=0.86,
                user_summary_hint="List overdue activities by account",
            )

        if re.search(r"\b(account|customer|company)\b", message):
            return ActionPlan(
                primary_agent="account-research",
                intent=Intent.SEARCH_ACCOUNTS.value,
                object_type="account",
                filters={},
                confidence=0.85,
            )

        if re.search(r"\b(opportunit(y|ies)|pipeline|deals?)\b", message):
            return ActionPlan(
                primary_agent="sales-rep",
                intent=Intent.SEARCH_OPPORTUNITIES.value,
                object_type="opportunity",
                filters={},
                confidence=0.88,
            )

        sys_id_match = re.search(r"\bsys_id[=:\s]+([a-f0-9]{32})\b", compiled.current_request, re.I)
        if sys_id_match:
            return ActionPlan(
                primary_agent=primary,
                intent=Intent.GET_RECORD.value,
                object_type="activity",
                filters={"sys_id": sys_id_match.group(1)},
                confidence=0.82,
            )

        return ActionPlan(
            primary_agent=primary,
            intent=Intent.UNKNOWN.value,
            confidence=0.40,
        )

    def generate_response(
        self,
        plan: ActionPlan,
        execution: PlanExecutionResult,
        compiled: CompiledPrompt,
    ) -> str:
        decision = execution.decision
        action = decision.decision_action.value
        status = decision.status
        context = decision.context or {}

        if action == "retrieve" and status == "connector_pending_credentials":
            return (
                f"I understood your request ({plan.intent}) and routed it through the "
                "SalesWon connector, but ServiceNow credentials are not yet configured. "
                "Once credentials are supplied, this query will return live data."
            )
        if action == "ask":
            missing = context.get("missing_fields", plan.missing_fields)
            q = context.get("clarifying_question") or plan.clarifying_question
            return q or f"I need a bit more information: {', '.join(missing)}."
        if action == "recommend":
            draft = execution.proposed_action or context.get("proposed_action", {})
            return (
                "Please confirm this activity update before I submit it:\n"
                f"{json.dumps(draft, indent=2)}"
            )
        if action == "refuse":
            return f"I cannot proceed: {status or 'policy violation'}."
        if action == "answer":
            count = len(execution.records)
            hint = plan.user_summary_hint or "your request"
            return f"Found {count} record(s) for {hint}."
        return plan.user_summary_hint or "Request processed."
