---
spec_version: "1.0.0"
spec_id: accountability-spec
title: SalesWon AI Accountability Specification
---

# Accountability Specification

Defines how Digital Employees are **accountable for outcomes, not just outputs**.

## Authority vs Accountability

| Question | Contract | File |
|----------|----------|------|
| *Can I do this?* | Authority | `AUTHORITY.md` |
| *Am I succeeding?* | Accountability | `ACCOUNTABILITY.md` |

Decision rights live in AUTHORITY — not duplicated here. ACCOUNTABILITY references AUTHORITY for decision rights only.

## Scope

Every Digital Employee and the Workforce Manager (spec) MUST implement `ACCOUNTABILITY.md` per [agent-spec.md](agent-spec.md).

## Required Sections (ACCOUNTABILITY.md)

1. **Mission** — links `MISSION.md`
2. **Responsibilities** — expected accomplishments
3. **Success criteria** — observable positive outcomes (CRM-linked where possible)
4. **Failure criteria** — observable negative signals
5. **Learning signals** — inputs for behavior improvement
6. **Ownership** — Owns / Supports / Does Not Own (distinct from COLLABORATION handoffs)
7. **Business KPIs** — links `METRICS.md` business section
8. **Operational KPIs** — links `METRICS.md` operational section

## Learning Signals (Workforce-Wide)

| Signal | Source | Use |
|--------|--------|-----|
| User edits | platform/feedback.md | Draft quality improvement |
| Approvals | audit log | Authority calibration |
| Rejections | feedback | Recommendation tuning |
| Escalations | audit log | Threshold review |
| Manager corrections | feedback + audit | Coaching loop |
| Customer outcomes | CRM + Phase 2 CSAT | Business KPI validation |

Ties to `MEMORY_LONG.md` (user-scoped only), `platform/feedback.md`, future reinforcement.

## Ownership vs Collaboration

| Concept | File | Focus |
|---------|------|-------|
| Ownership | ACCOUNTABILITY.md | Strategic accountability — what role owns as outcomes |
| Collaboration | COLLABORATION.md | Tactical handoffs — produces/consumes artifacts |

## Machine-Readable Contract

```yaml
spec_version: "1.0.0"
spec_id: accountability-spec
implements: agent-spec
required_sections:
  - mission
  - responsibilities
  - success_criteria
  - failure_criteria
  - learning_signals
  - ownership
  - business_kpis
  - operational_kpis
learning_signals:
  - user_edits
  - approvals
  - rejections
  - escalations
  - manager_corrections
  - customer_outcomes
ownership_categories:
  - owns
  - supports
  - does_not_own
decision_rights_reference: AUTHORITY.md
```

## References

- Implements: [agent-spec.md](agent-spec.md), [workforce-spec.md](workforce-spec.md)
- Implemented by: `agents/*/ACCOUNTABILITY.md`
