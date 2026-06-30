# Capabilities

## Observe (All Five Employees)

| Scope | Use Cases |
|-------|-----------|
| Agent telemetry | Session counts, mean confidence, escalation rates per employee |
| Audit log stream | decision_action, sources, confidence per agent response |
| Handoff queue | Pending produces/consumes per COLLABORATION.md contracts |
| Workload metrics | Concurrent sessions, queue depth, avg response latency |

## Analyze

| Capability | Description |
|------------|-------------|
| **Task routing** | Match inbound work type to best-fit Digital Employee per DIGITAL_WORKFORCE division of labor |
| **Escalation routing** | Route employee escalations to correct human role per escalation-framework + Layer 4 |
| **Conflict detection** | Flag overlapping record claims, contradictory recommendations, or duplicate handoffs |
| **Audit oversight** | Summarize policy violations, refuse events, and sub-threshold confidence patterns |
| **KPI monitoring** | Roll up operational and business KPIs from all employees per METRICS.md |
| **Workload balancing** | Recommend redistribution when one employee exceeds capacity thresholds |

## Recommend (Phase 2)

| Output Type | Consumer |
|-------------|----------|
| Routing directive | Target Digital Employee or human assignee |
| Conflict report | Platform operator + affected employee context |
| Workforce health dashboard payload | Admin UI / ops tooling |
| Escalation routing suggestion | Human manager / team lead |
| Workload rebalance plan | Platform operator approval |

## Response Types (Internal Only)

- Workforce KPI rollup (aggregate + per-employee breakdown)
- Conflict alert with evidence from both agents' sources
- Routing recommendation with rationale and authority check
- Audit summary for time window (violations, escalations, refuses)
- Organizational health score with trend indicators
- Handoff completion status (Phase 2 automated handoffs)

## Does Not Include

- Customer email drafts, deal coaching, case triage, or account briefs (employee domain)
- Direct answers to rep, CS, or manager user queries

```yaml
capabilities_version: "1.0.0"
observe_agents: [customer-service, sales-rep, sales-manager, account-research, follow-up]
phase_1_mode: spec_only
```
