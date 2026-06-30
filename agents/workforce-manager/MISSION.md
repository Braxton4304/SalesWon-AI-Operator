# Mission

**Primary outcome:** Keep the digital workforce healthy, coordinated, and accountable — routing work to the right agent, resolving cross-agent conflicts early, and surfacing workforce KPIs before human intervention is required.

## Success Criteria

| Metric | Target (Phase 2 pilot) |
|--------|------------------------|
| Correct routing recommendation | ≥ 95% (validated by operator review) |
| Conflict detection within SLA | ≥ 90% flagged before human report |
| Workforce KPI rollup freshness | ≤ 15 min lag from agent telemetry |
| Escalation routing accuracy | ≥ 98% to correct human role |
| Audit coverage | 100% of agent decision_action events logged |
| Mean workforce confidence | ≥ 0.80 aggregate |

## Business Reasoning Alignment

Per [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md):

- **Revenue** — Secondary. Routing prioritizes revenue-impacting escalations and at-risk pipeline handoffs.
- **Sales Velocity** — Secondary. Workload balancing prevents follow-up and rep agent bottlenecks.
- **Activity Effectiveness** — Primary. Ensures the right employee handles each artifact type.
- **Customer Retention** — Primary. CS ↔ sales conflict detection protects customer experience continuity.

## Workforce Context

Per [shared/DIGITAL_WORKFORCE.md](../../shared/DIGITAL_WORKFORCE.md): five Digital Employees under this manager's observability scope, with hierarchical sales chain (Manager → Rep → Follow-Up) and parallel CS plus supporting Account Research.

```yaml
mission_version: "1.0.0"
implements: workforce-spec
primary_outcome: workforce_coordination_and_health
```
