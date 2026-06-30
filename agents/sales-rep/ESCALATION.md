# Escalation

Implements: [specifications/governance-spec.md](../../specifications/governance-spec.md), [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md)

Set `escalation_required: true` and `decision_action: escalate` (or `refuse` where noted) when triggers fire.

## Mandatory

| Condition | Route To | Output |
|-----------|----------|--------|
| Discount/pricing approval needed | Sales manager / deal desk | escalation_required=true, refuse on commit |
| Legal/contract terms | Legal + manager | escalation_payload with urgency high |
| Opportunity ownership dispute | Sales ops | escalation_payload with record IDs |
| Confidence < 0.60 on deal financials after 3 retrieves | Manager review | missing_data + escalation_payload |
| Customer executive complaint on active deal | Manager + CS liaison | link case + opp in source_records |
| Product capability claim not in KB | Manager + SE | refuse unsupported claim |

## Conditional

| Condition | Route To | Output |
|-----------|----------|--------|
| Strategic account opp at Critical deal_health | Manager + account team | escalation_required if rep requests exception |
| Multi-year commit proposal | Deal desk | recommend manager review |
| Service risk (P1/P2) on active deal account | CS liaison + manager | flag in opportunity_summary; optional CS Agent handoff |
| rep_coaching_items conflict with next_best_action | Manager clarification | note conflict; defer to manager guidance |
| Blocking MEDDIC gaps within 7 days of close | Manager deal review | escalation_required on rep request for forecast uplift |

## Output Requirements

When escalating:

```json
{
  "escalation_required": true,
  "decision_action": "escalate",
  "escalation_payload": {
    "reason": "Discount request exceeds rep authority",
    "route_to": "sales_manager",
    "urgency": "standard"
  },
  "suggested_follow_up": { "type": "none" }
}
```

## Non-Escalation

- Qualification gaps → recommend + recommended_questions (not escalate unless rep requests manager involvement)
- Missing CRM fields → ask or missing_data (escalate only after retrieve exhaustion)
- Account research depth → suggest Account Research Agent (human-mediated handoff, not escalation)

```yaml
escalation_version: "1.1.0"
agent_id: sales-rep
output_field: escalation_required
phase: 1
autonomous_escalation_send: false
```
