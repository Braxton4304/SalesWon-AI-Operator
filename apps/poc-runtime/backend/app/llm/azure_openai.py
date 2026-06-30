# implements: runtime-spec

"""Azure OpenAI LLM adapter — activates when AZURE_OPENAI_* env vars are set."""

from __future__ import annotations

from typing import Any

import httpx

from app.config.settings import get_settings
from app.intent.schemas import Intent
from app.llm.base import FieldExtraction, IntentClassification, LLMNotConfigured, LLMProvider


class AzureOpenAIProvider(LLMProvider):
    def __init__(self) -> None:
        self._settings = get_settings()

    def _ensure_configured(self) -> None:
        if not self._settings.azure_openai_configured:
            raise LLMNotConfigured(
                "Azure OpenAI not configured. Set AZURE_OPENAI_* env vars."
            )

    def _chat(self, messages: list[dict[str, str]]) -> str:
        self._ensure_configured()
        url = (
            f"{self._settings.azure_openai_endpoint.rstrip('/')}"
            f"/openai/deployments/{self._settings.azure_openai_deployment}"
            "/chat/completions?api-version=2024-02-15-preview"
        )
        response = httpx.post(
            url,
            headers={
                "api-key": self._settings.azure_openai_api_key,
                "Content-Type": "application/json",
            },
            json={"messages": messages, "temperature": 0.3},
            timeout=30.0,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    def classify_intent(
        self, message: str, history: list[dict[str, str]]
    ) -> IntentClassification:
        self._ensure_configured()
        # TODO: structured output / function calling for intent classification
        _ = history
        content = self._chat(
            [
                {
                    "role": "system",
                    "content": (
                        "Classify the user intent as one of: search_opportunities, "
                        "search_activities, search_accounts, get_record, update_activity, unknown."
                    ),
                },
                {"role": "user", "content": message},
            ]
        )
        intent_str = content.strip().lower().replace(" ", "_")
        try:
            intent = Intent(intent_str)
        except ValueError:
            intent = Intent.UNKNOWN
        return IntentClassification(intent=intent, confidence=0.85, raw_text=message)

    def extract_fields(
        self, intent: Intent, message: str, history: list[dict[str, str]]
    ) -> FieldExtraction:
        self._ensure_configured()
        _ = history
        content = self._chat(
            [
                {
                    "role": "system",
                    "content": f"Extract JSON fields for intent {intent.value}.",
                },
                {"role": "user", "content": message},
            ]
        )
        # TODO: parse structured JSON from model response
        return FieldExtraction(fields={"raw": content}, missing_required=[], confidence=0.80)

    def generate_response(
        self,
        intent: Intent,
        decision_action: str,
        context: dict[str, Any],
    ) -> str:
        self._ensure_configured()
        return self._chat(
            [
                {
                    "role": "system",
                    "content": (
                        f"Generate a governed response for intent={intent.value}, "
                        f"action={decision_action}."
                    ),
                },
                {"role": "user", "content": str(context)},
            ]
        )
