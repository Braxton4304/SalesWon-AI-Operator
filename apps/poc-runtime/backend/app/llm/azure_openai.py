# implements: runtime-spec

"""Azure OpenAI LLM adapter — primary planning path with structured JSON output."""

from __future__ import annotations

import json
import logging

import httpx

from app.config.settings import get_settings
from app.llm.base import LLMNotConfigured, LLMProvider
from app.planning.results import PlanExecutionResult
from app.planning.schema import ActionPlan
from app.runtime.prompt_compiler import CompiledPrompt

logger = logging.getLogger(__name__)


class AzureOpenAIProvider(LLMProvider):
    def __init__(self) -> None:
        self._settings = get_settings()

    def _ensure_configured(self) -> None:
        if not self._settings.azure_openai_configured:
            raise LLMNotConfigured(
                "Azure OpenAI not configured. Set AZURE_OPENAI_* env vars."
            )

    def _chat(self, messages: list[dict[str, str]], json_mode: bool = False) -> str:
        self._ensure_configured()
        url = (
            f"{self._settings.azure_openai_endpoint.rstrip('/')}"
            f"/openai/deployments/{self._settings.azure_openai_deployment}"
            "/chat/completions?api-version=2024-02-15-preview"
        )
        body: dict = {
            "messages": messages,
            "temperature": 0.3,
        }
        if json_mode:
            body["response_format"] = {"type": "json_object"}

        response = httpx.post(
            url,
            headers={
                "api-key": self._settings.azure_openai_api_key,
                "Content-Type": "application/json",
            },
            json=body,
            timeout=60.0,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    def plan(self, compiled: CompiledPrompt) -> ActionPlan:
        self._ensure_configured()
        messages = [
            {"role": "system", "content": compiled.system_message},
            {"role": "developer", "content": compiled.developer_message},
            *compiled.messages,
        ]
        messages.append(
            {
                "role": "user",
                "content": (
                    "Respond with ONLY a JSON object matching the ActionPlan schema "
                    "for the latest user message. No markdown."
                ),
            }
        )
        raw = self._chat(messages, json_mode=True)
        try:
            data = json.loads(raw)
            return ActionPlan.model_validate(data)
        except (json.JSONDecodeError, ValueError) as exc:
            logger.warning("Azure plan parse failed: %s", exc)
            return ActionPlan(
                primary_agent=compiled.primary_agent,
                intent="unknown",
                confidence=0.3,
                clarifying_question="I could not parse a valid plan. Could you rephrase?",
                missing_fields=["intent"],
            )

    def generate_response(
        self,
        plan: ActionPlan,
        execution: PlanExecutionResult,
        compiled: CompiledPrompt,
    ) -> str:
        self._ensure_configured()
        payload = {
            "plan": plan.model_dump(),
            "decision_action": execution.decision.decision_action.value,
            "status": execution.decision.status,
            "record_count": len(execution.records),
            "proposed_action": execution.proposed_action,
        }
        return self._chat(
            [
                {"role": "system", "content": compiled.system_message},
                {
                    "role": "user",
                    "content": (
                        "Write a concise governed response for the sales user. "
                        "Do not fabricate CRM data. Use this execution result:\n"
                        f"{json.dumps(payload, default=str)}"
                    ),
                },
            ]
        )
