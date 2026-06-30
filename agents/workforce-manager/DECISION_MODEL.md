# Decision Model

## Routing Priority Order

1. **Safety and policy** — Refuse/violation events and legal/hostile escalations route first
2. **SLA and customer impact** — CS SLA breach risk and executive complaint escalations
3. **Revenue impact** — Critical pipeline health signals from sales-rep / sales-manager
4. **Handoff contract match** — Artifact type → designated consumer per COLLABORATION.md
5. **Employee capacity** — Prefer agent below 100% workload; defer if all saturated
6. **Confidence threshold** — Sub-0.60 employee outputs escalate before re-route

## Conflict Detection Matrix

| Scenario | Action |
|----------|--------|
| Two employees recommend contradictory CRM updates on same record | conflict report → human mediation |
| Duplicate handoff (same artifact, two producers) | flag producer; recommend canonical owner per DIGITAL_WORKFORCE |
| Employee routes outside domain (LIMITATIONS breach) | audit violation + refuse confirmation |
| CS case_summary conflicts with sales-rep opportunity_summary on same account | conflict report with account context |
| Follow-up and sales-rep both claim same activity draft | defer to sales-rep; follow-up supports |

## Workload Balancing Rules

| Condition | Action |
|-----------|--------|
| Employee > 120% capacity for > 15 min | recommend defer non-urgent work or reroute per division of labor |
| Account-research backlog > threshold | recommend sales-manager reprioritize research requests |
| All sales chain employees saturated | escalate to human ops; do not drop CS parallel queue |

## Scenario Matrix

| Scenario | Action |
|----------|--------|
| Unknown work type | ask operator for classification |
| Clear artifact + consumer in handoff matrix | recommend route to consumer |
| Escalation from any employee | match ESCALATION.md → human role |
| KPI poll | retrieve all employee metrics → aggregate |
| Phase 1 handoff event | log + recommend human mediation |

## Business Reasoning Weights

Activity Effectiveness 1.0, Customer Retention 1.0, Sales Velocity 0.9, Revenue 0.8

```yaml
decision_model_version: "1.0.0"
implements: workforce-spec
```
