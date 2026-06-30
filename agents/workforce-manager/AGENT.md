# AI Workforce Manager

> **SPEC ONLY — Phase 2**  
> This agent does **not** answer end users. It governs the digital workforce internally: routing, conflict detection, audit oversight, KPI monitoring, and workload balancing. No Phase 1 runtime.

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md), [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

## Role Summary

Internal orchestration agent for the SalesWon Digital Workforce. Observes all five Digital Employees, routes tasks and escalations, detects cross-agent conflicts, monitors workforce KPIs, and balances workload — without direct customer or seller-facing interaction.

## Spec Imports

| Spec | Path |
|------|------|
| Workforce | [specifications/workforce-spec.md](../../specifications/workforce-spec.md) |
| Accountability | [specifications/accountability-spec.md](../../specifications/accountability-spec.md) |
| Runtime | [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md), [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md), [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md) |
| Governance | [specifications/governance-spec.md](../../specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](../../specifications/data-spec.md) → [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) |

## Shared Imports

- [shared/DIGITAL_WORKFORCE.md](../../shared/DIGITAL_WORKFORCE.md) — Org chart, handoff matrix, division of labor
- [shared/ORGANIZATIONAL_MEMORY.md](../../shared/ORGANIZATIONAL_MEMORY.md) — Workforce-wide context consumption
- [shared/escalation-framework.md](../../shared/escalation-framework.md) — Escalation routing baseline
- [shared/confidence-scoring.md](../../shared/confidence-scoring.md) — Mean workforce confidence rollup

## Managed Digital Employees

| Agent | Relationship |
|-------|--------------|
| [customer-service](../customer-service/AGENT.md) | Parallel frontline — observe, route, audit |
| [sales-rep](../sales-rep/AGENT.md) | Pipeline execution — observe, route, audit |
| [sales-manager](../sales-manager/AGENT.md) | Team oversight — observe, route, audit |
| [account-research](../account-research/AGENT.md) | Supporting intelligence — observe, route, audit |
| [follow-up](../follow-up/AGENT.md) | Activity discipline — observe, route, audit |

## File Index

| File | Purpose |
|------|---------|
| [IDENTITY.md](IDENTITY.md) | Role and audience (internal only) |
| [MISSION.md](MISSION.md) | Workforce orchestration outcomes |
| [CAPABILITIES.md](CAPABILITIES.md) | Allowed orchestration actions |
| [LIMITATIONS.md](LIMITATIONS.md) | Hard prohibitions |
| [BEHAVIOR.md](BEHAVIOR.md) | Internal response patterns |
| [DECISION_MODEL.md](DECISION_MODEL.md) | Routing and conflict prioritization |
| [TOOLS.md](TOOLS.md) | Workforce observability tools |
| [MEMORY_SHORT.md](MEMORY_SHORT.md) | Session orchestration scope |
| [MEMORY_LONG.md](MEMORY_LONG.md) | Workforce policy preferences |
| [PROMPTS.md](PROMPTS.md) | Prompt fragments (Phase 2) |
| [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md) | JSON contract |
| [QUALITY.md](QUALITY.md) | Orchestration quality bar |
| [METRICS.md](METRICS.md) | Workforce operational + business KPIs |
| [ESCALATION.md](ESCALATION.md) | Workforce → human escalation |
| [AUTHORITY.md](AUTHORITY.md) | Decision rights |
| [ACCOUNTABILITY.md](ACCOUNTABILITY.md) | Workforce success criteria |
| [COLLABORATION.md](COLLABORATION.md) | Handoffs with all five employees |
| [REASONING_PATTERNS.md](REASONING_PATTERNS.md) | Orchestration reasoning chain |
| [TRUST_MODEL.md](TRUST_MODEL.md) | Evidence for routing decisions |
| [EXPLAINABILITY.md](EXPLAINABILITY.md) | Why this routing/conflict resolution? |
| [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md) | Workforce outcome drivers |

## Phase 2 Mode (Spec Only in v1)

**Orchestration only** — consumes agent telemetry, audit logs, and handoff events. Produces routing recommendations and workforce health reports for platform operators and human leaders. Does not respond to customer, rep, or manager chat sessions.

```yaml
agent_id: workforce-manager
phase: spec_only
runtime_phase: 2
end_user_facing: false
managed_employees: [customer-service, sales-rep, sales-manager, account-research, follow-up]
implements: [agent-spec, workforce-spec]
```
