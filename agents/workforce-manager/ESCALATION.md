# Escalation

Implements: [shared/escalation-framework.md](../../shared/escalation-framework.md), [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

## Escalation Chain

```text
Digital Employee → Workforce Manager (Phase 2) → Human Leader / Platform Ops
```

Phase 1: employees escalate directly to humans per employee ESCALATION.md; Workforce Manager documents routing rules only.

## Mandatory (Workforce Manager → Human)

| Condition | Route To |
|-----------|----------|
| Unresolved cross-agent conflict (severity high/critical) | Platform ops + affected human team lead |
| Policy violation cluster (≥ 3 refuses in 1 hr same agent) | Platform admin + governance review |
| All employees saturated > 130% capacity | Human ops / workforce admin |
| Audit log integrity failure or missing telemetry | Platform engineering |
| Routing ambiguity — no clear employee owner | Workforce administrator |
| Legal / hostile communication escalated from any employee | Designated Layer 4 contact |

## Conditional

- Mean workforce confidence < 0.65 for > 1 hr → human leader review
- Handoff completion rate < 80% (Phase 2) → process review with ops
- Repeated routing overrides by operators → policy update ADR

## Employee Escalation Routing (Workforce Manager Recommends)

| Source Employee | Common Triggers | Human Target |
|-----------------|-----------------|--------------|
| customer-service | SLA breach, legal, hostile | CS team lead |
| sales-rep | Pricing, ownership dispute | Sales manager / deal desk |
| sales-manager | Forecast commit, territory | Sales director |
| account-research | Data conflict, strategic account | Sales ops + manager |
| follow-up | Rep non-response, exec touchpoint | Sales manager |

## Output

`decision_action: escalate` with `recommended_action.type: human_escalation` and Layer 4 assignee role.

```yaml
escalation_version: "1.0.0"
chain: [digital_employee, workforce_manager, human]
phase_1_direct_to_human: true
```
