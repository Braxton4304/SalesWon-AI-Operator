# Output Schema

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md), [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "WorkforceManagerAgentOutput",
  "type": "object",
  "required": [
    "summary",
    "confidence",
    "sources",
    "decision_action",
    "workforce_health",
    "affected_agents"
  ],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Internal operator-facing summary — not end-user text"
    },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "sources": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "id"],
        "properties": {
          "type": { "enum": ["crm", "kb", "policy", "audit", "telemetry"] },
          "id": { "type": "string" },
          "label": { "type": "string" },
          "agent_id": { "type": "string" }
        }
      }
    },
    "decision_action": {
      "enum": ["answer", "ask", "retrieve", "escalate", "refuse", "recommend"]
    },
    "workforce_health": {
      "enum": ["healthy", "strained", "critical"]
    },
    "affected_agents": {
      "type": "array",
      "items": {
        "enum": [
          "customer-service",
          "sales-rep",
          "sales-manager",
          "account-research",
          "follow-up"
        ]
      }
    },
    "routing_recommendation": {
      "type": "object",
      "properties": {
        "target_agent_id": { "type": "string" },
        "target_human_role": { "type": "string" },
        "work_type": { "type": "string" },
        "rationale": { "type": "string" },
        "authority_check_passed": { "type": "boolean" },
        "human_mediated": { "type": "boolean", "default": true }
      }
    },
    "conflict_alert": {
      "type": "object",
      "properties": {
        "conflict_id": { "type": "string" },
        "severity": { "enum": ["low", "medium", "high", "critical"] },
        "agents_involved": { "type": "array", "items": { "type": "string" } },
        "record_id": { "type": "string" },
        "contradiction_summary": { "type": "string" },
        "recommended_mediation": { "type": "string" }
      }
    },
    "kpi_rollup": {
      "type": "object",
      "properties": {
        "mean_workforce_confidence": { "type": "number" },
        "cross_agent_escalation_rate": { "type": "number" },
        "handoff_completion_rate": { "type": "number" },
        "per_agent_metrics": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "agent_id": { "type": "string" },
              "mean_confidence": { "type": "number" },
              "escalation_rate": { "type": "number" },
              "capacity_pct": { "type": "number" },
              "telemetry_freshness": { "type": "string", "format": "date-time" }
            }
          }
        }
      }
    },
    "workload_balance_plan": {
      "type": "object",
      "properties": {
        "overloaded_agents": { "type": "array", "items": { "type": "string" } },
        "defer_actions": { "type": "array", "items": { "type": "string" } },
        "reroute_actions": { "type": "array", "items": { "type": "string" } }
      }
    },
    "audit_summary": {
      "type": "object",
      "properties": {
        "window_start": { "type": "string", "format": "date-time" },
        "window_end": { "type": "string", "format": "date-time" },
        "refuse_count": { "type": "integer" },
        "escalate_count": { "type": "integer" },
        "sub_confidence_count": { "type": "integer" },
        "by_agent": { "type": "object" }
      }
    },
    "recommended_action": {
      "type": "object",
      "properties": {
        "type": {
          "enum": [
            "routing_directive",
            "conflict_report",
            "workload_rebalance",
            "human_escalation"
          ]
        },
        "target_agent_id": { "type": "string" },
        "draft_payload": { "type": "object" }
      }
    },
    "clarifying_question": { "type": "string" }
  }
}
```

## Example

```json
{
  "summary": "Workforce Strained: Follow-Up at 142% capacity; 8 stalled handoffs from sales-rep. Recommend defer non-urgent cadence checks.",
  "confidence": 0.93,
  "sources": [
    { "type": "telemetry", "id": "wf-20260630-001", "label": "Workforce telemetry snapshot", "agent_id": "follow-up" },
    { "type": "audit", "id": "audit-handoff-44", "label": "Stalled opportunity_summary handoffs" }
  ],
  "decision_action": "recommend",
  "workforce_health": "strained",
  "affected_agents": ["follow-up", "sales-rep"],
  "kpi_rollup": {
    "mean_workforce_confidence": 0.84,
    "cross_agent_escalation_rate": 0.04,
    "handoff_completion_rate": 0.91,
    "per_agent_metrics": [
      { "agent_id": "follow-up", "mean_confidence": 0.86, "escalation_rate": 0.02, "capacity_pct": 142, "telemetry_freshness": "2026-06-30T14:00:00Z" }
    ]
  },
  "workload_balance_plan": {
    "overloaded_agents": ["follow-up"],
    "defer_actions": ["Defer low-priority cadence nudges for 2 hours"],
    "reroute_actions": []
  },
  "recommended_action": {
    "type": "workload_rebalance",
    "draft_payload": { "operator_approval_required": true }
  }
}
```
