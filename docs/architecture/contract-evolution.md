# Contract Evolution

Path from markdown specifications to executable runtime contracts.

## Vision

Each document in `/specifications` and implementation folders defines a **contract** consumable by:

1. **Humans** — architects, developers, Cursor agents
2. **CI** — validation in pull requests
3. **Runtime SDK** — parsers and enforcers

## Evolution Stages

### Stage 1 — Markdown Contracts (Current)

- YAML/JSON fenced blocks in `.md` files
- Manual review in PRs
- Cursor rules enforce conventions

### Stage 2 — JSON Schema Validation (Planned)

- Extract machine-readable blocks to `schemas/*.json`
- CI validates:
  - `runtime/CONFIG.yaml` against runtime-spec schema
  - Agent `OUTPUT_SCHEMA.md` blocks against agent-spec schema
  - `DATA_DICTIONARY.md` entries against data-spec schema

### Stage 3 — Runtime Parsers (Planned)

- SDK loads specs at startup
- Fail fast on invalid agent folders (pattern: AI Council validator)
- Decision engine reads DECISION_ENGINE contract

### Stage 4 — Published Spec Package (Planned)

- `@saleswon/ai-specs` npm or Python package
- Versioned releases independent of customer deployments
- Cohort, Axiom, AI Council import by version pin

## Contract Requirements

Every contract file SHOULD include:

```yaml
spec_version: "1.0.0"
implements: parent-spec-id  # if implementation
```

Every machine block SHOULD be valid JSON or YAML parseable without prose.

## ADR Required For

- Breaking spec version bumps
- New required agent files
- data-spec permission level changes

Record in [architecture/DECISIONS.md](../../architecture/DECISIONS.md).

## Reference Implementations

Patterns borrowed from:

- AI Council `INTERFACES.md` machine blocks and folder validator
- Directing Messaging governed AI checklist
- OpenClaw tool allowlists (future runtime CONFIG)

Not inherited wholesale — SalesWon specs remain independent IP.
