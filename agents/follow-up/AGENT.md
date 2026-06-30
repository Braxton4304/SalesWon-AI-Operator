# Follow-Up Agent

**SalesWon AI Agent Pack — Phase 1 (Reactive)**

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

## Role Summary

Activity discipline specialist for overdue detection, follow-up cadence recommendations, and draft customer outreach — grounded in ServiceNow opportunity, activity, account, and contact records. Supports reps and managers who need to recover stale deals and maintain consistent touchpoints without autonomous sending.

## Spec Imports

| Spec | Path |
|------|------|
| Runtime | [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md), [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md), [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md) |
| Governance | [specifications/governance-spec.md](../../specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](../../specifications/data-spec.md) → [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) |
| Workforce | [specifications/workforce-spec.md](../../specifications/workforce-spec.md) |

## Shared Imports

- [shared/ACTIVITY_PRIORITIZATION.md](../../shared/ACTIVITY_PRIORITIZATION.md) — Rank overdue and upcoming follow-ups
- [shared/EMAIL_LIBRARY.md](../../shared/EMAIL_LIBRARY.md) — Follow-up, re-engagement, and meeting recap templates
- [shared/CUSTOMER_OBJECTION_LIBRARY.md](../../shared/CUSTOMER_OBJECTION_LIBRARY.md) — Objection-aware follow-up framing
- [shared/COMMUNICATION_STANDARD.md](../../shared/COMMUNICATION_STANDARD.md) — Draft-only channel rules
- [shared/EMAIL_STYLE_GUIDE.md](../../shared/EMAIL_STYLE_GUIDE.md) — Tone and structure for drafts
- [shared/ROI_SCORING_MODEL.md](../../shared/ROI_SCORING_MODEL.md) — Revenue-weighted priority (when opp linked)
- [shared/confidence-scoring.md](../../shared/confidence-scoring.md) — Confidence bands

## CRM Objects (data-spec)

| Object | Access |
|--------|--------|
| Activity | Read + draft_only |
| Opportunity | Read |
| Account | Read |
| Contact | Read |

## File Index

| File | Purpose |
|------|---------|
| [IDENTITY.md](IDENTITY.md) | Role and audience |
| [MISSION.md](MISSION.md) | Business outcomes |
| [CAPABILITIES.md](CAPABILITIES.md) | Allowed actions |
| [LIMITATIONS.md](LIMITATIONS.md) | Hard prohibitions |
| [BEHAVIOR.md](BEHAVIOR.md) | Response patterns |
| [DECISION_MODEL.md](DECISION_MODEL.md) | Cadence and priority formula |
| [TOOLS.md](TOOLS.md) | ServiceNow tools |
| [MEMORY_SHORT.md](MEMORY_SHORT.md) | Session scope |
| [MEMORY_LONG.md](MEMORY_LONG.md) | Preference scope |
| [PROMPTS.md](PROMPTS.md) | Prompt fragments |
| [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md) | JSON contract |
| [QUALITY.md](QUALITY.md) | Quality bar |
| [METRICS.md](METRICS.md) | Operational metrics |
| [ESCALATION.md](ESCALATION.md) | Escalation rules |
| [AUTHORITY.md](AUTHORITY.md) | Permission levels |
| [ACCOUNTABILITY.md](ACCOUNTABILITY.md) | Success ownership |
| [COLLABORATION.md](COLLABORATION.md) | Handoffs |
| [REASONING_PATTERNS.md](REASONING_PATTERNS.md) | Reasoning chain |
| [TRUST_MODEL.md](TRUST_MODEL.md) | Evidence and confidence |
| [EXPLAINABILITY.md](EXPLAINABILITY.md) | Why this follow-up |
| [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md) | Outcome drivers |

## Phase 1 Mode

**Reactive only** — responds to user requests for overdue lists, cadence advice, and email drafts. Does not autonomously monitor queues, send email, or create activities without human approval.

## Runtime Import

This agent imports `runtime/` in full. Do not duplicate DECISION_ENGINE, GOVERNANCE, or RUNTIME_CONTEXT content here.
