# Architecture Decision Log

Record significant decisions here (ADR-style). Spec changes MUST have an entry before merging.

## Format

```markdown
## ADR-NNN: Title

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Superseded
**Spec affected:** platform-spec | runtime-spec | agent-spec | governance-spec | data-spec

### Context
What is the issue?

### Decision
What was decided?

### Consequences
What are the tradeoffs?
```

---

## ADR-001: Spec-First Contract Architecture

**Date:** 2026-06-30
**Status:** Accepted
**Spec affected:** platform-spec

### Context

SalesWon AI must be reusable IP across SalesWon, Cohort, Axiom, and AI Council — not loose documentation tied to one implementation.

### Decision

Establish `/specifications` as the authoritative contract layer. All other folders implement specs. Add `data-spec.md` for CRM access as a first-class contract.

### Consequences

- Spec changes require ADR entries
- Implementations link upward to specs
- Future SDK parses machine-readable blocks in spec files

---

## ADR-002: Enterprise Agent Files Replace SOUL.md

**Date:** 2026-06-30
**Status:** Accepted
**Spec affected:** agent-spec

### Context

Anthomorphic persona files (`SOUL.md`) do not resonate with enterprise architects.

### Decision

Use operational files: IDENTITY, MISSION, CAPABILITIES, LIMITATIONS, BEHAVIOR, DECISION_MODEL. Split memory (SHORT/LONG) and evaluation (QUALITY/METRICS).

### Consequences

- Clearer observable system behavior
- Better alignment with CTO/architect review
