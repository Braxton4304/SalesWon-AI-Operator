# implements: agent-spec

"""Select primary Digital Employee for a turn."""

from __future__ import annotations

from app.agent.manifest import load_manifest
from app.planning.schema import ActionPlan


def select_primary_agent(plan: ActionPlan | None = None, message: str = "") -> str:
    manifest = load_manifest()
    if plan and plan.primary_agent in manifest.agent_ids():
        return plan.primary_agent

    msg = message.lower()
    domain_map = {
        "follow-up": ["follow-up", "follow up", "overdue", "reschedule", "friday", "tomorrow"],
        "account-research": ["account", "research", "brief", "stakeholder", "contact"],
        "customer-service": ["case", "ticket", "support", "incident", "sla"],
        "sales-rep": ["opportunity", "deal", "pipeline", "quarter", "forecast", "activity", "call"],
    }
    for agent_id, keywords in domain_map.items():
        if agent_id in manifest.agent_ids() and any(k in msg for k in keywords):
            return agent_id
    return manifest.agents[0].id if manifest.agents else "sales-rep"
