# Escalation

Role-specific escalation rules. Mandatory triggers from [shared/escalation-framework.md](../../shared/escalation-framework.md) always apply.

## Mandatory Escalation (This Agent)

| Condition | Route To |
|-----------|----------|
| Confidence < 0.60 after 3 retrieve cycles | Sales Manager (human) or RevOps analyst |
| Team pipeline view inaccessible or empty after retries | RevOps / CRM admin |
| Manager visibility boundary error (403/scope) | Platform admin + human manager |
| Legal or compliance keyword in forecast/commit context | Legal contact (Layer 4) |
| User says "speak to a human" | Next available sales leader or RevOps |
| Forecast commit or territory reassignment requested and persisted | refuse + route to human with write access |
| Material quota/compensation dispute detected in request | HR / sales leadership (Layer 4) |

## Optional Escalation

| Condition | Route To |
|-----------|----------|
| Single commit deal > 30% of team quota at critical risk | Regional VP |
| P1 case on commit-category account | CS leadership + account executive |
| Rep performance pattern across 3+ consecutive reviews | HR business partner (Layer 4) |
| Conflicting opp data between team view and opp record | RevOps data steward |
| Strategic/tier-1 account commit at critical risk | Account executive + regional VP |

## Escalation Payload

Include per escalation-framework:

```yaml
escalation_payload:
  request: original manager question
  attempted_actions: [tool calls and retrieve cycles]
  confidence: numeric score
  sources: source_records summary
  forecast_risks_summary: top 3 at-risk opps if applicable
  suggested_assignee: role or Layer 4 contact
  manager_actions_draft: proposed interim actions
```

## Escalation vs. Refuse

| Situation | Action |
|-----------|--------|
| Cannot access data — retriable | retrieve → escalate |
| User asks agent to commit forecast | refuse (not escalate) |
| User asks agent to reassign territory | refuse (not escalate) |
| Team scope ambiguous | ask (not escalate) |
| Critical deal risk — manager can act | answer with manager_actions; optional notify VP |

## Layer 4 Configuration

Customer-specific contacts, assignment groups, and VP routing — not in this repo.

```yaml
escalation_version: "1.0.0"
agent_id: sales-manager
mandatory_triggers: 7
default_route: sales_manager_human
```
