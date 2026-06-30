# Short Memory

- Active routing evaluation context (work item ID, classification candidates)
- Open conflict queue (conflict_id, agents_involved, severity)
- Current workforce KPI snapshot timestamp per employee
- Pending escalation routing decisions awaiting operator ack
- Workload balance plan under review

Re-query telemetry when operator may have applied manual routing mid-session.

## Task States

`routing_evaluation`, `conflict_review`, `kpi_rollup`, `audit_summary`, `workload_rebalance`, `escalation_routing`

```yaml
memory_short_version: "1.0.0"
scope: session_orchestration
```
