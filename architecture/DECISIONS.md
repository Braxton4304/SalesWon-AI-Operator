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

---

## ADR-003: Digital Workforce v1 — Digital Employees

**Date:** 2026-06-30
**Status:** Accepted
**Spec affected:** agent-spec, workforce-spec

### Context

Five independent agent folders insufficient for client demo. Need governed division-of-labor roles.

### Decision

Five Digital Employees: customer-service, sales-rep, sales-manager, account-research, follow-up. Add COLLABORATION.md, REASONING_PATTERNS.md, mathematical DECISION_MODEL, split METRICS, full OUTPUT_SCHEMA pipeline.

### Consequences

- Handoffs human-mediated in Phase 1
- Workforce Manager spec deferred to ADR-004 path

---

## ADR-004: AIMS Layer — Policies, Authority, Trust, Explainability

**Date:** 2026-06-30
**Status:** Accepted
**Spec affected:** workforce-spec, agent-spec, platform-spec

### Context

Digital Employees need enterprise realism: authority limits, trust contracts, explainability, organizational policies.

### Decision

Add `policies/` layer, `workforce-spec.md`, per-agent AUTHORITY.md, TRUST_MODEL.md, EXPLAINABILITY.md, BUSINESS_OBJECTIVES.md, shared/ORGANIZATIONAL_MEMORY.md, agents/workforce-manager/ (spec only).

### Consequences

- 21 files per agent before accountability (now 22 per ADR-005)
- Internal framing: Enterprise AI Management System (AIMS)

---

## ADR-005: Accountability Spec and Architecture Freeze

**Date:** 2026-06-30
**Status:** Accepted
**Spec affected:** accountability-spec, agent-spec

### Context

Digital Employees must be accountable for outcomes, not just outputs. Architecture at risk of unbounded expansion.

### Decision

1. Add `accountability-spec.md` as 7th canonical spec
2. Add `ACCOUNTABILITY.md` to every Digital Employee (22-file set complete)
3. **Freeze architecture:** no new spec domains or architecture files without ADR
4. Shift effort from breadth to depth (enterprise content in each agent)

### Consequences

- Seven-spec set is closed until ADR
- Every agent answers "Am I succeeding?" via ACCOUNTABILITY.md
- Authority (can do) vs accountability (succeeded) explicitly separated

---

## ADR-006: Runnable POC Code in `/apps/poc-runtime/`

**Date:** 2026-06-30
**Status:** Accepted
**Spec affected:** platform-spec, runtime-spec, governance-spec, data-spec

### Context

The repository is spec-first: `/runtime` and `/platform` hold authoritative markdown contracts, not executable code. Phase 1 requires a locally runnable POC shell (chat UI, `/chat` API, connector contracts, scope enforcement) that implements those contracts without polluting spec folders or adding an 8th specification domain.

### Decision

1. Add top-level `/apps/poc-runtime/` as the home for runnable POC code:
   - `backend/` — FastAPI application implementing runtime-spec, governance-spec, data-spec
   - `frontend/` — React + Vite chat UI
2. Keep `/runtime` and `/platform` as markdown-only contracts; POC code references them via `implements:` headers.
3. No fake demo data; connector and LLM surfaces are stubbed until real credentials are supplied.
4. Technical documentation lives in `/docs/poc-runtime/`.

### Consequences

- Clear separation between contracts and implementation
- POC can be deleted or replaced without touching spec files
- Future Runtime SDK (Phase 2) may migrate patterns from `/apps/poc-runtime/` into a dedicated package
- Does not add a new spec domain; implements existing frozen specs per ADR-005

---

## ADR-007: Unscripted Agent Runtime in POC

**Date:** 2026-06-30
**Status:** Accepted
**Spec affected:** runtime-spec, agent-spec, data-spec, governance-spec

### Context

ADR-006 delivered a connector-ready POC shell with regex-based intent routing (`RuleBasedLLMProvider`). Client demo requires unscripted natural-language planning using Azure OpenAI and the existing Digital Employee specs in `/agents/`, while preserving governed execution (scope enforcement, confirmation before writes, audit logging).

### Decision

1. Extend `/apps/poc-runtime/backend/` with:
   - `ActionPlan` structured planning contract (`app/planning/`)
   - Agent contract loader reading from `/agents/` via `config/poc_agent_manifest.yaml`
   - Prompt compiler implementing `runtime/RUNTIME_CONTEXT.md` assembly order
   - Azure OpenAI as default LLM provider with `plan()` + structured JSON output
   - `PlanValidator` + `PlanExecutor` — LLM plans, backend validates, connector executes
2. Core rule: **LLM plans. Backend validates. Connector executes. User confirms writes.**
3. `RuleBasedLLMProvider` retained as offline/CI fallback only when Azure creds are missing.
4. `config/saleswon_mapping.yaml` defines object/table/field mappings (TODO until SalesWon credentials).
5. No new spec domain; implements frozen specs per ADR-005.

### Consequences

- POC becomes a real agent runtime demo, not a scripted routing shell
- Single UI assistant; multiple Digital Employee specs compiled internally
- Full `SalesRepAgentOutput` schema deferred to Phase 2 SDK; slim `ActionPlan` used for execution
- Prompt context size managed via POC-trimmed agent file subsets in manifest
