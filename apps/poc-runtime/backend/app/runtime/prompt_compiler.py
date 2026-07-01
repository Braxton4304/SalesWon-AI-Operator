# implements: runtime-spec, runtime/RUNTIME_CONTEXT.md

"""Compile governed runtime prompt from agent specs, policies, and session state."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from app.agent.loader import compile_agent_context
from app.agent.selector import select_primary_agent
from app.memory.short_term import SessionState
from app.planning.mapping_loader import mapping_summary_for_prompt
from app.planning.schema import ActionPlan
from app.security.user_context import CurrentUserContext


@dataclass
class CompiledPrompt:
    system_message: str
    developer_message: str
    messages: list[dict[str, str]]
    user_context: CurrentUserContext
    session_id: str
    current_request: str
    primary_agent: str
    extra: dict[str, Any] = field(default_factory=dict)


PLANNING_RULES = """
You are the SalesWon AI planning layer. Output ONLY valid JSON matching the ActionPlan schema.

Rules:
- NEVER execute CRM writes yourself. Set requires_confirmation=true for any update_activity plan.
- NEVER fabricate CRM data. If information is missing, populate missing_fields and clarifying_question.
- Supported intents: search_opportunities, search_activities, search_accounts, get_record, update_activity, unknown.
- v1 writes: update_activity only. All other write intents → intent unknown or refuse via unsupported fields.
- Scope: user only sees records they own (enforced by backend).
- primary_agent must be one of: sales-rep, follow-up, account-research, customer-service.
"""


class PromptCompiler:
    def compile(
        self,
        ctx: CurrentUserContext,
        session: SessionState,
        message: str,
        pending_context: dict[str, Any] | None = None,
    ) -> CompiledPrompt:
        primary_agent = select_primary_agent(message=message)
        if pending_context and pending_context.get("primary_agent"):
            primary_agent = pending_context["primary_agent"]

        agent_context = compile_agent_context(primary_agent)
        mapping_summary = mapping_summary_for_prompt()

        system_message = (
            "SalesWon AI — governed Digital Employee runtime.\n"
            "LLM plans. Backend validates. Connector executes. User confirms writes.\n"
            "Never fabricate CRM field values."
        )

        schema_json = json.dumps(ActionPlan.json_schema(), indent=2)
        developer_message = (
            f"{PLANNING_RULES}\n\n"
            f"ActionPlan JSON schema:\n{schema_json}\n\n"
            f"CRM mapping:\n{mapping_summary}\n\n"
            f"Tenant: {ctx.tenant_id}\nUser: {ctx.user_id}\nRoles: {', '.join(ctx.roles)}"
        )

        messages: list[dict[str, str]] = []
        for turn in session.turns:
            messages.append({"role": turn["role"], "content": turn["content"]})

        if pending_context:
            messages.append(
                {
                    "role": "system",
                    "content": f"Pending clarification context: {json.dumps(pending_context)}",
                }
            )

        messages.append({"role": "user", "content": message})

        return CompiledPrompt(
            system_message=system_message,
            developer_message=developer_message + f"\n\n## Agent contracts\n{agent_context}",
            messages=messages,
            user_context=ctx,
            session_id=session.session_id,
            current_request=message,
            primary_agent=primary_agent,
            extra={"agent_context_length": len(agent_context)},
        )
