# Accountability

Implements: [specifications/accountability-spec.md](../../specifications/accountability-spec.md)

**Am I succeeding?** (Distinct from AUTHORITY and COLLABORATION.)

## Mission

Link [MISSION.md](MISSION.md) — workforce coordination, conflict prevention, KPI visibility, and audit oversight across five Digital Employees.

## Responsibilities

- Monitor and report workforce health across all five Digital Employees
- Route tasks and escalations to the correct employee or human role
- Detect and surface cross-agent conflicts before they impact customers or pipeline
- Maintain audit oversight of agent decision_action compliance
- Roll up operational and business KPIs per workforce-spec
- Balance workload when employees exceed capacity thresholds
- Enforce handoff contract integrity per COLLABORATION.md

## Success Criteria

- Routing recommendations validated correct ≥ 95% by operators
- Conflicts detected and reported before external stakeholder impact ≥ 90%
- Workforce KPI dashboards fresh within 15 minutes
- Zero unaudited agent decision events in production
- Mean workforce confidence maintained ≥ 0.80
- Escalation routing to correct human role ≥ 98%

## Failure Criteria

- End-user-facing response issued by Workforce Manager
- Incorrect routing causing SLA breach or duplicate employee work
- Undetected high-severity conflict on shared CRM record
- KPI rollup with fabricated or unstale-labeled missing data
- CRM write attempted by Workforce Manager
- Employee authority overridden without approval audit trail

## Learning Signals

- operator_routing_overrides — calibrate classify_work_item rules
- conflict_mediation_outcomes — tune detection severity thresholds
- human_escalation_feedback — refine ESCALATION.md routing table
- workload_rebalance_acceptance — adjust capacity thresholds
- audit_violation_trends — governance review triggers
- kpi_anomaly_alerts — employee performance correlation

## Ownership

| Owns | Supports | Does Not Own |
|------|----------|--------------|
| Workforce routing recommendations | All five employees' operational visibility | Customer case resolution |
| Cross-agent conflict detection | Human leader escalation routing | Opportunity execution |
| Workforce KPI aggregation | Audit compliance reporting | Pipeline forecasting |
| Workload balance plans | Handoff queue monitoring | Account research content |
| Organizational health scoring | Platform ops incident response | Activity cadence drafts |

## KPIs

See [METRICS.md](METRICS.md) — Operational (Workforce Manager), Operational (Aggregate), and Business sections.

```yaml
accountability_version: "1.0.0"
implements: accountability-spec
managed_employees: [customer-service, sales-rep, sales-manager, account-research, follow-up]
```
