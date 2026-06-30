# SalesWon Digital Workforce v1

Technical documentation for the Digital Workforce v1 deliverable.

## Overview

SalesWon Digital Workforce v1 implements five **Digital Employees** as governed role specifications inside the SalesWon AI Operating System. Each employee has 22 contract files implementing seven frozen specifications.

Internal product category: **Enterprise AI Management System (AIMS)**.

## Specification Stack

| Spec | File |
|------|------|
| Platform | specifications/platform-spec.md |
| Runtime | specifications/runtime-spec.md |
| Agent | specifications/agent-spec.md (v1.1, 22 files) |
| Governance | specifications/governance-spec.md |
| Data | specifications/data-spec.md |
| Workforce | specifications/workforce-spec.md |
| Accountability | specifications/accountability-spec.md |

## Policy Layer

Enterprise policies in `policies/` — inherited by all agents. See policies/README.md.

## Agent Roster

| Agent ID | Files | Phase |
|----------|-------|-------|
| customer-service | 22 | 1 reactive |
| sales-rep | 22 | 1 reactive |
| sales-manager | 22 | 1 reactive |
| account-research | 22 | 1 reactive |
| follow-up | 22 | 1 reactive |
| workforce-manager | 22 | Spec only (Phase 2) |

## Key Contracts Per Agent

- **AUTHORITY.md** — Observe → Analyze → Recommend → Draft → Request Approval → Execute (empty v1)
- **ACCOUNTABILITY.md** — Success/failure criteria, learning signals, ownership
- **DECISION_MODEL.md** — Weighted priority formula (deterministic)
- **OUTPUT_SCHEMA.md** — Input → Processing → Output → Confidence → Escalation → Audit
- **COLLABORATION.md** — Handoff produces/consumes YAML

## Architecture Freeze

ADR-005: No new spec domains without ADR in architecture/DECISIONS.md.

## Next Steps (Phase 2)

- Runtime SDK implementing decision engine formulas
- Workforce Manager orchestration
- ServiceNow connector
- Accountability learning loops via platform/feedback.md

## References

- agents/README.md
- shared/DIGITAL_WORKFORCE.md
- docs/implementation/getting-started.md
