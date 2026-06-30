# Metrics

Implements: [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

## Operational (Workforce Manager)

| Metric | Target |
|--------|--------|
| Schema compliance | ≥ 99% |
| Routing recommendation accuracy (operator validated) | ≥ 95% |
| Conflict detection rate (true positives / reported conflicts) | ≥ 90% |
| KPI rollup freshness | ≤ 15 min lag |
| Escalation routing accuracy | ≥ 98% |
| Audit coverage of agent events | 100% |
| Mean orchestration confidence | ≥ 0.85 |

## Operational (Aggregate Workforce)

Per workforce-spec — rolled up from all five employees:

| Metric | Target |
|--------|--------|
| Mean workforce confidence | ≥ 0.80 |
| Cross-agent escalation rate | Track; target decline Phase 2 |
| Handoff completion rate | ≥ 90% (Phase 2 automated handoffs) |
| Per-employee schema compliance | ≥ 99% each |

## Business

- Organizational health uptime (% time workforce_health = healthy)
- Time-to-mediate conflicts (operator ack → resolution)
- Workload rebalance acceptance rate by operators
- Revenue-impacting escalation response time (sales chain)
- CS SLA breach prevention via routing (correlation study Phase 2)

## Per-Employee Rollup Sources

| Agent | Primary Metrics Imported |
|-------|-------------------------|
| customer-service | Case triage accuracy, SLA awareness, escalation rate |
| sales-rep | Next-best-action acceptance, opp fact accuracy |
| sales-manager | Forecast risk identification, pipeline rollup accuracy |
| account-research | Brief completeness, signal detection rate |
| follow-up | Cadence compliance, overdue activity recovery |

```yaml
metrics_version: "1.0.0"
implements: workforce-spec
aggregate_kpis: [mean_workforce_confidence, cross_agent_escalation_rate, handoff_completion_rate]
```
