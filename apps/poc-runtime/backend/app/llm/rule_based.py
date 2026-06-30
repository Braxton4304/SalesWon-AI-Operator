# implements: runtime-spec

"""Deterministic rule-based LLM stub for local development."""

from __future__ import annotations

import re
from typing import Any

from app.intent.schemas import Intent
from app.llm.base import FieldExtraction, IntentClassification, LLMProvider

_INTENT_PATTERNS: list[tuple[Intent, re.Pattern[str], float]] = [
    (
        Intent.SEARCH_OPPORTUNITIES,
        re.compile(r"\b(opportunit(y|ies)|pipeline|deals?)\b", re.I),
        0.88,
    ),
    (
        Intent.SEARCH_ACTIVITIES,
        re.compile(r"\b(activit(y|ies)|tasks?|calls?|meetings?)\b", re.I),
        0.86,
    ),
    (
        Intent.SEARCH_ACCOUNTS,
        re.compile(r"\b(account|customer|company)\b", re.I),
        0.85,
    ),
    (
        Intent.GET_RECORD,
        re.compile(r"\b(show|get|fetch|details? for|record)\b", re.I),
        0.82,
    ),
    (
        Intent.UPDATE_ACTIVITY,
        re.compile(r"\b(update|mark|complete|close|change)\b.*\b(activity|call|task)\b", re.I),
        0.90,
    ),
    (
        Intent.UPDATE_ACTIVITY,
        re.compile(r"\b(update|mark|complete)\b", re.I),
        0.75,
    ),
]

_UNSUPPORTED = re.compile(
    r"\b(send email|delete|create opportunity|update opportunity|forecast)\b", re.I
)


class RuleBasedLLMProvider(LLMProvider):
    def classify_intent(
        self, message: str, history: list[dict[str, str]]
    ) -> IntentClassification:
        _ = history
        if _UNSUPPORTED.search(message):
            return IntentClassification(
                intent=Intent.UNKNOWN, confidence=0.95, raw_text=message
            )
        for intent, pattern, confidence in _INTENT_PATTERNS:
            if pattern.search(message):
                return IntentClassification(
                    intent=intent, confidence=confidence, raw_text=message
                )
        return IntentClassification(
            intent=Intent.UNKNOWN, confidence=0.40, raw_text=message
        )

    def extract_fields(
        self, intent: Intent, message: str, history: list[dict[str, str]]
    ) -> FieldExtraction:
        _ = history
        fields: dict[str, Any] = {}
        missing: list[str] = []

        account_match = re.search(r"\bfor\s+([A-Za-z0-9\s\-]+?)(?:\s+to|\s*$)", message, re.I)
        if account_match:
            fields["account_name"] = account_match.group(1).strip()

        status_match = re.search(r"\bto\s+(done|complete|completed|closed|open)\b", message, re.I)
        if status_match:
            fields["status"] = status_match.group(1).lower()

        sys_id_match = re.search(r"\bsys_id[=:\s]+([a-f0-9]{32})\b", message, re.I)
        if sys_id_match:
            fields["sys_id"] = sys_id_match.group(1)

        if intent == Intent.UPDATE_ACTIVITY:
            if "sys_id" not in fields and "account_name" not in fields:
                missing.append("activity_identifier")
            if "status" not in fields:
                missing.append("status")

        if intent == Intent.GET_RECORD and "sys_id" not in fields:
            missing.append("sys_id")

        confidence = 0.90 if not missing else 0.65
        return FieldExtraction(fields=fields, missing_required=missing, confidence=confidence)

    def generate_response(
        self,
        intent: Intent,
        decision_action: str,
        context: dict[str, Any],
    ) -> str:
        status = context.get("status")
        if decision_action == "retrieve" and status == "connector_pending_credentials":
            return (
                f"I understood your request ({intent.value}) and routed it through the "
                "SalesWon connector, but ServiceNow credentials are not yet configured. "
                "Once credentials are supplied, this query will return live data."
            )
        if decision_action == "ask":
            missing = context.get("missing_fields", [])
            return f"I need a bit more information: {', '.join(missing)}."
        if decision_action == "recommend":
            draft = context.get("proposed_action", {})
            return (
                "Please confirm this activity update before I submit it:\n"
                f"{draft}"
            )
        if decision_action == "refuse":
            return f"I cannot proceed: {status or 'policy violation'}."
        if decision_action == "answer":
            records = context.get("records", [])
            count = len(records)
            return f"Found {count} record(s) matching your request."
        return context.get("message", "Request processed.")
