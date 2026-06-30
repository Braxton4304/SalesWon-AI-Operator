# implements: runtime-spec

"""LLM provider factory."""

from __future__ import annotations

from app.config.settings import get_settings
from app.llm.azure_openai import AzureOpenAIProvider
from app.llm.base import LLMProvider
from app.llm.rule_based import RuleBasedLLMProvider


def get_llm_provider() -> LLMProvider:
    settings = get_settings()
    if settings.llm_provider == "azure_openai":
        return AzureOpenAIProvider()
    return RuleBasedLLMProvider()
