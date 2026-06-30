# Capabilities

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md), [AUTHORITY.md](AUTHORITY.md)

## Read

| Object | Use Cases |
|--------|-----------|
| **Opportunity** | Stage, amount, probability, close date, next step, competitors, contacts, forecast category |
| **Account** | Tier, industry, parent account, open opps/cases |
| **Contact** | Stakeholders, roles, engagement history |
| **Activity** | Past calls, emails, tasks, overdue items |
| **Lead** | Pre-opportunity qualification status |

## Draft-Only Writes (recommend)

| Object | Draft Types |
|--------|-------------|
| **Opportunity** | next_step update, stage change proposal, meeting notes summary |
| **Activity** | Call task, email follow-up, meeting prep task |
| **Lead** | Qualification notes, conversion recommendation |

## Response Types

- `opportunity_summary` — deal context with financials, stage, stakeholders
- `deal_health` — Healthy | At Risk | Critical per PIPELINE_HEALTH_MODEL
- `qualification_gaps` — MEDDIC/SPIN/Sandler fields missing in CRM
- `next_best_action` — ranked activity with DECISION_MODEL priority_score
- `recommended_questions` — discovery/qualification questions by methodology
- `suggested_follow_up` — email or activity draft (EMAIL_STYLE_GUIDE)
- Meeting prep brief (account + opp + recent activities)
- Objection handling talking points (SALES_PLAYBOOK ch. 5)
- "What should I work on today?" — ranked opp/activity list for user's pipeline

## Methodology Application

| Stage | Primary Framework | Output |
|-------|-------------------|--------|
| Early / Discovery | SPIN + Sandler pain | recommended_questions (Situation, Problem, Implication) |
| Mid / Qualification | MEDDIC + Sandler budget | qualification_gaps, recommended_questions |
| Late / Proposal | MEDDIC completeness | qualification_gaps (blocking severity), next_best_action |

## Playbook Chapters Used

Discovery (1), Qualification (2), Proposal prep (3), Objection Handling (5)

## Authority Alignment

All writes are `draft` → `recommend` per [AUTHORITY.md](AUTHORITY.md). No autonomous send or CRM commit.
