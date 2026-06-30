---
spec_version: "1.0.0"
spec_id: workforce-spec
title: SalesWon AI Workforce Specification
---

# Workforce Specification

Defines the digital organizational structure, collaboration contracts, authority inheritance, and future orchestration rules for the SalesWon Digital Workforce.

## Scope

- Organizational hierarchy (Digital Employees + Workforce Manager)
- Authority inheritance (POLICIES + per-agent AUTHORITY.md)
- Collaboration and handoff contracts (COLLABORATION.md)
- Escalation contracts (employee → manager → human)
- Workforce-level KPIs
- Organizational memory consumption
- Future orchestration (Workforce Manager — Phase 2)

Implements: [accountability-spec.md](accountability-spec.md), [agent-spec.md](agent-spec.md)

Implementation: [shared/DIGITAL_WORKFORCE.md](../shared/DIGITAL_WORKFORCE.md), [agents/workforce-manager/](../agents/workforce-manager/)

## Digital Employees (Phase 1)

| Agent | Role |
|-------|------|
| customer-service | Service case triage and communication |
| sales-rep | Opportunity execution and discovery |
| sales-manager | Pipeline, forecast, coaching |
| account-research | Account intelligence and briefs |
| follow-up | Activity discipline and cadence |

## Workforce Manager (Spec Only — Phase 2 Runtime)

Does not answer end users. Governs: workload balancing, task routing, escalation routing, conflict detection, audit oversight, KPI monitoring, organizational health.

## Hierarchy

```text
Workforce Manager (Phase 2)
        │
Sales Manager Agent
        ↓
Sales Rep Agent
        ↓
Follow-Up Agent

Parallel: Customer Service Agent
Supporting: Account Research Agent
```

## Authority Inheritance

```text
policies/ → runtime/GOVERNANCE → agent/AUTHORITY.md → agent/LIMITATIONS.md
```

Manager roles may `request_approval` paths that employees cannot. Workforce Manager observes all employees in Phase 2.

## Handoff Contract Schema

Each COLLABORATION.md MUST include:

```yaml
produces: [{artifact, schema_ref, consumer_agents}]
consumes: [{artifact, source_agent, trigger}]
handoff_triggers: [{event, target_agent, human_mediated: true}]
```

Phase 1: all handoffs `human_mediated: true`.

## Workforce KPIs (Aggregate)

- Mean workforce confidence
- Cross-agent escalation rate
- Handoff completion rate (Phase 2)
- Business KPI rollup per DIGITAL_WORKFORCE.md

## Machine-Readable Contract

```yaml
spec_version: "1.0.0"
spec_id: workforce-spec
digital_employees:
  - customer-service
  - sales-rep
  - sales-manager
  - account-research
  - follow-up
workforce_manager:
  phase: spec_only
  runtime_phase: 2
handoff_mode_phase_1: human_mediated
authority_inheritance:
  - policies/
  - runtime/GOVERNANCE.md
  - agents/*/AUTHORITY.md
organizational_memory: shared/ORGANIZATIONAL_MEMORY.md
```

## References

- Implements: [platform-spec.md](platform-spec.md), [accountability-spec.md](accountability-spec.md)
- Implemented by: [shared/DIGITAL_WORKFORCE.md](../shared/DIGITAL_WORKFORCE.md)
