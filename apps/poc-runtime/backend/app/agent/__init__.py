"""Agent contract loader."""

from app.agent.loader import compile_agent_context, load_all_agent_ids
from app.agent.manifest import load_manifest
from app.agent.selector import select_primary_agent

__all__ = [
    "compile_agent_context",
    "load_all_agent_ids",
    "load_manifest",
    "select_primary_agent",
]
