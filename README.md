# SalesWon AI Operator

**SalesWon AI Operating System** — Enterprise AI Management System (AIMS) for governed digital employees.

Contract-first foundation for every SalesWon deployment and reusable IP for Cohort, Axiom, and AI Council.

**Architecture frozen** (7 specs) — no new spec domains without ADR. See [architecture/DECISIONS.md](architecture/DECISIONS.md) ADR-005.

## Start Here

1. [specifications/](specifications/) — 7 canonical contracts
2. [shared/DIGITAL_WORKFORCE.md](shared/DIGITAL_WORKFORCE.md) — org chart
3. [agents/](agents/) — five Digital Employees (22 files each)

## Architecture

```text
/specifications     ← 7 contracts (FROZEN)
/policies           ← Enterprise policies
/runtime            ← Orchestration + governance
/shared             ← Playbooks + organizational memory
/agents             ← Digital Employees + Workforce Manager spec
/platform           ← ServiceNow, data dictionary, RAG
/architecture       ← Design workspace + ADRs
```

## Digital Workforce v1

| Employee | Folder |
|----------|--------|
| Customer Service | [agents/customer-service/](agents/customer-service/) |
| Sales Rep | [agents/sales-rep/](agents/sales-rep/) |
| Sales Manager | [agents/sales-manager/](agents/sales-manager/) |
| Account Research | [agents/account-research/](agents/account-research/) |
| Follow-Up | [agents/follow-up/](agents/follow-up/) |
| Workforce Manager (spec) | [agents/workforce-manager/](agents/workforce-manager/) |

## Specification Index (7)

| Spec | File |
|------|------|
| Platform | [platform-spec.md](specifications/platform-spec.md) |
| Runtime | [runtime-spec.md](specifications/runtime-spec.md) |
| Agent | [agent-spec.md](specifications/agent-spec.md) |
| Governance | [governance-spec.md](specifications/governance-spec.md) |
| Data | [data-spec.md](specifications/data-spec.md) |
| Workforce | [workforce-spec.md](specifications/workforce-spec.md) |
| Accountability | [accountability-spec.md](specifications/accountability-spec.md) |

## Documentation

- [docs/architecture/platform-layers.md](docs/architecture/platform-layers.md)
- [docs/implementation/getting-started.md](docs/implementation/getting-started.md)

## IP

SalesWon AI Operating System v1 — Power Tech intellectual property.
