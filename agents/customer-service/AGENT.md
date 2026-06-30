# Customer Service Agent

**SalesWon AI Agent Pack — Phase 1 (Reactive)**

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

## Role Summary

Frontline ServiceNow CSM assistant for case triage, ITIL impact/urgency assessment, SLA-aware status summaries, and draft customer communications — grounded in case, account, and contact records per CUSTOMER_SERVICE_FRAMEWORK.

## Spec Imports

| Spec | Path |
|------|------|
| Runtime | [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md), [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md), [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md) |
| Governance | [specifications/governance-spec.md](../../specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](../../specifications/data-spec.md) → [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) |
| Workforce | [specifications/workforce-spec.md](../../specifications/workforce-spec.md) |
| Accountability | [specifications/accountability-spec.md](../../specifications/accountability-spec.md) |

## Shared Imports

- [shared/CUSTOMER_SERVICE_FRAMEWORK.md](../../shared/CUSTOMER_SERVICE_FRAMEWORK.md) — tier handling, sentiment rules, SLA awareness
- [shared/COMMUNICATION_STANDARD.md](../../shared/COMMUNICATION_STANDARD.md) — channel policies (email draft_only)
- [shared/EMAIL_STYLE_GUIDE.md](../../shared/EMAIL_STYLE_GUIDE.md) — customer-facing draft format
- [shared/escalation-framework.md](../../shared/escalation-framework.md) — mandatory escalation triggers
- [shared/confidence-scoring.md](../../shared/confidence-scoring.md) — confidence bands

## Policy Imports

- [policies/COMMUNICATION_POLICY.md](../../policies/COMMUNICATION_POLICY.md)
- [policies/EMAIL_POLICY.md](../../policies/EMAIL_POLICY.md)
- [policies/CUSTOMER_PROMISES.md](../../policies/CUSTOMER_PROMISES.md)
- [policies/PII_POLICY.md](../../policies/PII_POLICY.md)
- [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md)

## CRM Objects (data-spec)

| Object | Access |
|--------|--------|
| Case | Read + draft_only (comments, work notes, state proposals) |
| Account | Read |
| Contact | Read |
| Activity | Read + draft_only (follow-up tasks) |

## File Index

| File | Purpose |
|------|---------|
| [IDENTITY.md](IDENTITY.md) | Role and audience |
| [MISSION.md](MISSION.md) | Business outcomes |
| [CAPABILITIES.md](CAPABILITIES.md) | Allowed actions |
| [LIMITATIONS.md](LIMITATIONS.md) | Hard prohibitions |
| [BEHAVIOR.md](BEHAVIOR.md) | Response patterns |
| [DECISION_MODEL.md](DECISION_MODEL.md) | ITIL impact/urgency weights (100%) |
| [TOOLS.md](TOOLS.md) | ServiceNow tools |
| [MEMORY_SHORT.md](MEMORY_SHORT.md) | Session scope |
| [MEMORY_LONG.md](MEMORY_LONG.md) | Preference scope |
| [PROMPTS.md](PROMPTS.md) | Prompt fragments |
| [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md) | JSON contract + pipeline |
| [QUALITY.md](QUALITY.md) | Quality bar + demo scenarios |
| [METRICS.md](METRICS.md) | Operational + business KPIs |
| [ESCALATION.md](ESCALATION.md) | Escalation rules |
| [AUTHORITY.md](AUTHORITY.md) | Decision rights (6-level ladder) |
| [ACCOUNTABILITY.md](ACCOUNTABILITY.md) | Outcome ownership |
| [COLLABORATION.md](COLLABORATION.md) | Handoffs and artifacts |
| [REASONING_PATTERNS.md](REASONING_PATTERNS.md) | Reasoning chain |
| [TRUST_MODEL.md](TRUST_MODEL.md) | Evidence and confidence |
| [EXPLAINABILITY.md](EXPLAINABILITY.md) | Recommendation rationale |
| [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md) | Outcome drivers |

## Phase 1 Mode

**Reactive only** — responds to user requests. Does not autonomously monitor queues, send communications, or close cases.

## Primary Artifacts

- `case_summary` — structured case context consumed by Sales Manager Agent (service risk) and Workforce Manager
- `suggested_customer_response` — draft customer communication for human send per EMAIL_POLICY
