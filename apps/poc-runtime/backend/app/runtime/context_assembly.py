# implements: runtime-spec, runtime/RUNTIME_CONTEXT.md

"""Context assembly for governed LLM invocations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.security.user_context import CurrentUserContext


@dataclass
class RuntimeContext:
    system_prompt: str
    agent_prompt: str
    customer_configuration: dict[str, Any]
    crm_context: dict[str, Any] | None
    knowledge_context: dict[str, Any] | None
    user_behavior_signals: dict[str, Any] | None
    conversation_history: list[dict[str, str]]
    current_request: str
    user_context: CurrentUserContext
    extra: dict[str, Any] = field(default_factory=dict)


def assemble_context(
    user_ctx: CurrentUserContext,
    message: str,
    history: list[dict[str, str]],
    crm_context: dict[str, Any] | None = None,
    extra: dict[str, Any] | None = None,
) -> RuntimeContext:
    return RuntimeContext(
        system_prompt=(
            "You are SalesWon AI POC Runtime. Governed responses only. "
            "Never fabricate CRM data."
        ),
        agent_prompt="Single-agent POC shell — sales-rep read/update scope.",
        customer_configuration={"layer": 4, "status": "stub"},
        crm_context=crm_context,
        knowledge_context=None,
        user_behavior_signals=None,
        conversation_history=history,
        current_request=message,
        user_context=user_ctx,
        extra=extra or {},
    )
