# Cursor Rules (Source)

Copy these to `.cursor/rules/` as `.mdc` files when agent mode is available.

---

## platform-scope.mdc

```yaml
---
description: SalesWon AI Platform workspace charter
alwaysApply: true
---
```

This conversation is the system architecture and engineering workspace for the SalesWon AI project. Focus on: product requirements, AI architecture, Azure infrastructure, ServiceNow integration, database design, frontend/backend, governance, security, testing, deployment, technical roadmap.

Avoid pricing, contracts, commercialization, licensing, or partnership strategy unless they directly impact technical architecture.

Start from [specifications/](../../specifications/) before implementing.

---

## spec-first.mdc

```yaml
---
description: Specifications before implementation; contracts not prose
alwaysApply: true
---
```

1. Read relevant file in `specifications/` before changing runtime, agents, platform, or shared.
2. Spec changes require ADR in `architecture/DECISIONS.md`.
3. New files include `implements:` reference and machine-readable YAML/JSON block where applicable.
4. data-spec changes precede DATA_DICTIONARY changes.

---

## agent-spec-v1.mdc

```yaml
---
description: Enforce SalesWon agent-spec required files
globs: agents/**
alwaysApply: false
---
```

Required: AGENT.md, IDENTITY, MISSION, CAPABILITIES, LIMITATIONS, BEHAVIOR, DECISION_MODEL, TOOLS, MEMORY_SHORT, MEMORY_LONG, PROMPTS, OUTPUT_SCHEMA, QUALITY, METRICS, ESCALATION.

Forbidden: SOUL.md, MEMORY.md, EVALUATION.md.

Agents import runtime/ — do not duplicate governance.

---

## runtime-governance.mdc

```yaml
---
description: Runtime and governance conventions
globs: runtime/**
alwaysApply: false
---
```

Implement runtime-spec and governance-spec. No model-only answers. Tenant isolation required. See CONFIG.yaml (or CONFIG.md until YAML created).

---

## out-of-scope.mdc

```yaml
---
description: Block commercial topics unless architecture impact
alwaysApply: true
---
```

Do not discuss pricing, contracts, licensing, or partnerships unless the user explicitly ties them to a technical architecture decision.

```
