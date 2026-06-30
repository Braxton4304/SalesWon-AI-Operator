# Metrics

## Operational Metrics

| Metric | Target (90-day pilot) | Description |
|--------|----------------------|-------------|
| Schema compliance | ≥ 99% | OUTPUT_SCHEMA validation pass rate |
| Mean response latency | TBD Layer 4 | Time from request to valid JSON |
| Retrieve rate | Monitor | % turns requiring extra CRM/KB fetch |
| Escalation rate | Monitor | % turns ending escalate |
| Ask rate | Monitor | % turns needing case number clarification |

## Quality Metrics

| Metric | Target (90-day pilot) |
|--------|----------------------|
| Case fact accuracy (spot audit) | ≥ 95% |
| Hallucinated case fields | 0 tolerated |
| ITIL assessment alignment | ≥ 90% vs. CRM priority on audit |
| Source grounding | ≥ 98% of factual claims in source_records |
| Inappropriate escalation rate | < 5% |
| Severity formula compliance | ≥ 90% on audit sample |

## Usage Metrics

| Metric | Description |
|--------|-------------|
| Draft acceptance rate | suggested_customer_response used with ≤ 20% edit |
| Mean confidence | Target ≥ 0.82 |
| ITIL triage requests | % turns requesting impact/urgency assessment |
| Account case list requests | % multi-case triage turns |

## Business KPIs

| KPI | Driver | Target |
|-----|--------|--------|
| SLA breach prevention | sla_proximity factor + at_risk flag | Flag ≥ 24h before breach when SLA data available |
| First-response prep time | suggested_customer_response acceptance | Reduce rep draft time ≥ 30% (survey) |
| Escalation appropriateness | escalation_required accuracy | ≤ 5% inappropriate |
| Customer sentiment handling | CUSTOMER_SERVICE_FRAMEWORK compliance | Acknowledgment in 100% of frustrated-case drafts |
| Case summary reuse | case_summary artifact quality | Sales Manager cites without correction (Phase 2) |

## Collection

Audit records per governance-spec; feedback via [platform/feedback.md](../../platform/feedback.md).

Link to [ACCOUNTABILITY.md](ACCOUNTABILITY.md) success/failure criteria and [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md) drivers.

```yaml
metrics_version: "1.0.0"
agent_id: customer-service
kpi_categories: [operational, quality, usage, business]
```
