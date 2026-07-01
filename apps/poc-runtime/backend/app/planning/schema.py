# implements: runtime-spec, data-spec, agent-spec

"""ActionPlan schema — structured LLM output contract."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from app.intent.schemas import Intent


class ActionPlan(BaseModel):
    """
    Structured plan produced by LLM. Backend validates and executes — LLM never writes CRM.
    """

    primary_agent: str = Field(default="sales-rep", description="Digital Employee id")
    intent: str = Field(description="Connector intent: search_opportunities, search_activities, etc.")
    object_type: str | None = None
    filters: dict[str, Any] = Field(default_factory=dict)
    proposed_patch: dict[str, Any] | None = None
    missing_fields: list[str] = Field(default_factory=list)
    requires_confirmation: bool = False
    clarifying_question: str | None = None
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    user_summary_hint: str | None = None

    def to_intent(self) -> Intent:
        try:
            return Intent(self.intent)
        except ValueError:
            return Intent.UNKNOWN

    @classmethod
    def json_schema(cls) -> dict[str, Any]:
        return cls.model_json_schema()

    def plan_fields_for_executor(self) -> dict[str, Any]:
        """Map plan filters + patch into executor field dict."""
        fields = dict(self.filters)
        if self.proposed_patch:
            fields.update(self.proposed_patch)
        if self.filters.get("sys_id"):
            fields["sys_id"] = self.filters["sys_id"]
        return fields
