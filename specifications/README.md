# Specifications

**SalesWon AI Agent Specification v1** — contract layer (ISO-style).

These files are the authoritative contracts. All other folders in this repository **implement** them. Other products (Cohort, Axiom, AI Council) may reference these specifications without copying implementation folders.

## Spec Index

| Spec | Purpose |
|------|---------|
| [platform-spec.md](platform-spec.md) | Platform layers, boundaries, extension rules |
| [runtime-spec.md](runtime-spec.md) | Context assembly, decision engine, memory tiers |
| [agent-spec.md](agent-spec.md) | Agent file dictionary, OUTPUT_SCHEMA, import contract |
| [governance-spec.md](governance-spec.md) | Audit, confidence, escalation, security, tenant isolation |
| [data-spec.md](data-spec.md) | CRM objects, field requirements, read/write, confidence, ownership |

## Contract Format

Every spec file includes:

1. **Human-readable prose** — meaning for architects and developers
2. **Machine-readable block** — fenced JSON/YAML for future runtime parsing
3. **Version header** — `spec_version` in frontmatter

## Implementation Map

| Spec | Implemented by |
|------|----------------|
| platform-spec.md | `architecture/`, `platform/`, root layout |
| runtime-spec.md | `runtime/` |
| agent-spec.md | `agents/` |
| governance-spec.md | `runtime/GOVERNANCE.md`, `runtime/SECURITY.md`, `shared/confidence-scoring.md`, `shared/escalation-framework.md` |
| data-spec.md | `platform/DATA_DICTIONARY.md`, `platform/servicenow.md`, `platform/database.md` |

## Evolution Path

See [docs/architecture/contract-evolution.md](../docs/architecture/contract-evolution.md):

```
Markdown contracts → JSON Schema validation → Runtime parsers → SDK modules
```
