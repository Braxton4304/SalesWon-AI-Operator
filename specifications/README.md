# Specifications

**SalesWon AI Operating System** — canonical contract layer (7 specs, **architecture frozen**).

External name: SalesWon AI **Operating System**. Internal: Enterprise AI **Management System (AIMS)**.

These files are authoritative contracts. All other folders **implement** them. Cohort, Axiom, and AI Council may reference specs without copying implementations.

## Spec Index (Frozen — no 8th spec without ADR)

| Spec | Purpose |
|------|---------|
| [platform-spec.md](platform-spec.md) | Platform layers, boundaries, extension rules |
| [runtime-spec.md](runtime-spec.md) | Context assembly, decision engine, memory tiers |
| [agent-spec.md](agent-spec.md) | Digital Employee file dictionary (22 files) |
| [governance-spec.md](governance-spec.md) | Audit, confidence, escalation, security |
| [data-spec.md](data-spec.md) | CRM objects, permissions, confidence |
| [workforce-spec.md](workforce-spec.md) | Org hierarchy, collaboration, orchestration |
| [accountability-spec.md](accountability-spec.md) | Outcomes, success/failure, learning signals |

## Architecture Freeze

No new specification domains without ADR in [architecture/DECISIONS.md](../architecture/DECISIONS.md). See ADR-005.

## Contract Format

1. Human-readable prose
2. Machine-readable YAML/JSON block
3. `spec_version` in frontmatter

## Implementation Map

| Spec | Implemented by |
|------|----------------|
| platform-spec.md | Root layout, `architecture/`, `platform/` |
| runtime-spec.md | `runtime/` |
| agent-spec.md | `agents/` (22 files per Digital Employee) |
| governance-spec.md | `runtime/GOVERNANCE.md`, `runtime/SECURITY.md`, `policies/`, `shared/confidence-scoring.md` |
| data-spec.md | `platform/DATA_DICTIONARY.md`, `platform/servicenow.md` |
| workforce-spec.md | `shared/DIGITAL_WORKFORCE.md`, `agents/workforce-manager/` |
| accountability-spec.md | `agents/*/ACCOUNTABILITY.md` |

## Evolution Path

[docs/architecture/contract-evolution.md](../docs/architecture/contract-evolution.md)
