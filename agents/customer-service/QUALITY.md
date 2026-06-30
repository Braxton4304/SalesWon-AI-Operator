# Quality

Correctness, completeness, and hallucination avoidance criteria for this agent.

## Correctness

- [ ] Case number, state, priority, assignee match ServiceNow query
- [ ] SLA times computed from platform fields, not estimated
- [ ] Account/contact names match linked records
- [ ] ITIL impact and urgency align with case fields or documented inference rationale
- [ ] severity maps to DECISION_MODEL priority_score bands
- [ ] priority_score uses weights summing to 100% (35/30/15/10/10)
- [ ] Draft content reflects actual case issue, not generic template
- [ ] escalation_required true only when ESCALATION.md trigger applies
- [ ] Tenant and user visibility rules respected

## Completeness

- [ ] All required OUTPUT_SCHEMA fields present (including empty arrays where applicable)
- [ ] case_summary populated with core case fields or gaps in missing_data
- [ ] impact, urgency, severity present for triage requests
- [ ] suggested_customer_response present when user requests draft
- [ ] source_records cover all cases referenced in summary and recommendations
- [ ] missing_data lists absent required fields with impact description
- [ ] escalation_reason populated when escalation_required is true

## Hallucination Avoidance

- [ ] No case numbers cited without query confirmation
- [ ] Sentiment labeled `unknown` when insufficient text
- [ ] No promised resolution dates outside SLA policy or CUSTOMER_PROMISES
- [ ] KB suggestions cite `type: kb` source in source_records
- [ ] No ITIL scores without case field or inference citation
- [ ] No customer-facing commitments beyond draft recommendation

## Demo Scenarios

| # | Scenario | Expected Output |
|---|----------|-----------------|
| 1 | Open case summary with SLA on_track | Complete schema; case_summary; severity medium/low; escalation_required false |
| 2 | At-risk case with email draft | suggested_customer_response; decision_action recommend; SLA at_risk |
| 3 | High impact + high urgency production outage | severity critical; priority_score ≥ 0.75; escalation_required per SLA |
| 4 | Missing case number | decision_action ask; clarifying_question |
| 5 | Refund request | decision_action refuse; escalation_required true; billing route |
| 6 | VIP account frustrated sentiment | escalation_required true; account tier in source_records |
| 7 | Case missing assigned_to (required field) | missing_data; confidence reduced; escalate if unresolvable |
| 8 | Account case list — 5 open cases | case_summary.related_cases ranked by priority_score |
| 9 | Legal threat keywords | escalation_required true; no customer draft; legal route |
| 10 | ITIL fields in CRM | impact/urgency from case fields; high confidence |
| 11 | ITIL fields absent — infer from description | impact/urgency inferred; missing_data; confidence penalty |
| 12 | Confidence < 0.60 after 3 retrieves | decision_action escalate |

## Evaluation Harness (Planned)

Automated validation against OUTPUT_SCHEMA + golden case datasets. See [architecture/domains/testing-deployment](../../architecture/domains/testing-deployment/README.md).

```yaml
quality_version: "1.0.0"
agent_id: customer-service
demo_scenario_count: 12
decision_model_weights_sum: 100
```
