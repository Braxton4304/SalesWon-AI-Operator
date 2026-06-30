# Escalation

Mandatory triggers from [shared/escalation-framework.md](../../shared/escalation-framework.md) always apply.

## Mandatory Escalation

Set `escalation_required: true` and populate `escalation_reason` with trigger ID and narrative.

| Trigger ID | Condition | Route To | Payload |
|------------|-----------|----------|---------|
| SLA-BREACH | SLA breached + no resolution path | Team lead / on-call queue | case_summary + last 3 work notes |
| SLA-IMMINENT | SLA < 2h + no recent activity | Team lead | case_summary + recommended_action |
| LEGAL | Legal, lawsuit, regulatory keywords | Legal / compliance group (Layer 4) | Full case thread; no customer draft |
| SAFETY | Safety or harassment report | Security / HR per policy | Immediate; no AI draft to customer |
| USER-REQUEST | User: "escalate to manager" | Next available lead | User request + case context |
| LOW-CONF | Confidence < 0.60 after 3 retrieves | Senior CS rep | Blocking reason + partial findings |
| BILLING | Billing/refund/credit request | Billing team | Refuse customer commitment; escalate |
| REQUIRED-FIELD | case required fields absent after retrieve | Team lead | missing_data list per data-spec |

## Conditional Escalation

| Trigger ID | Condition | Route To |
|------------|-----------|----------|
| VIP-SENTIMENT | VIP/strategic account + frustrated/angry sentiment | Account CSM + team lead |
| MULTI-P1 | 3+ open P1/critical cases same account | Major incident coordinator |
| DUPLICATE-PATTERN | 5+ similar cases in 7 days | Problem management |
| ITIL-CRITICAL | severity critical + priority_score ≥ 0.75 + no owner action 4h | Tier 2 / on-call |

## Do Not Escalate

- Routine status questions with complete case data → **answer** (`escalation_required: false`)
- Draft iteration requests → **recommend** (same case)
- ITIL informational assessment with on_track SLA → **answer**

## ServiceNow Routing (Layer 4)

- Assignment groups: `CSM Tier 2`, `CSM Leadership`, `Legal Review`, `Billing Support`
- Map in customer deployment config

## Escalation Output

Use `decision_action: escalate` when routing to human queue. Include:

- `escalation_required: true`
- `escalation_reason`: trigger ID + human-readable rationale
- `recommended_action.type: escalation` with suggested group in draft_payload
- Full escalation payload per escalation-framework (request, attempted actions, confidence, sources)

```yaml
escalation_version: "1.0.0"
agent_id: customer-service
framework: shared/escalation-framework.md
output_fields: [escalation_required, escalation_reason]
```
