# implements: runtime-spec

"""LLM provider factory — Azure OpenAI primary, rule_based fallback."""

from __future__ import annotations

import logging

from app.config.settings import get_settings
from app.llm.azure_openai import AzureOpenAIProvider
from app.llm.base import LLMNotConfigured, LLMProvider
from app.llm.rule_based import RuleBasedLLMProvider

logger = logging.getLogger(__name__)


def get_llm_provider() -> LLMProvider:
    settings = get_settings()
    prefer_azure = settings.llm_provider == "azure_openai"

    if prefer_azure and settings.azure_openai_configured:
        return AzureOpenAIProvider()

    if prefer_azure and not settings.azure_openai_configured:
        logger.warning(
            "LLM_PROVIDER=azure_openai but Azure creds missing; falling back to rule_based"
        )

    return RuleBasedLLMProvider()
