# Capabilities

## Read

| Object | Use Cases |
|--------|-----------|
| **Activity** | Due date, state, type, assignee, last update, linked opp/account |
| **Opportunity** | Stage, amount, probability, close date, next step, owner — for priority weighting |
| **Account** | Tier, industry, open opps — for strategic cadence |
| **Contact** | Recipient for drafts, role, last engagement |

## Draft-Only Writes (recommend)

| Object | Draft Types |
|--------|-------------|
| **Activity** | Follow-up call task, email task, meeting reschedule proposal |
| **Email** | Re-engagement, post-meeting recap, overdue check-in (via draft_email) |

## Response Types

- Overdue activity list ranked by ACTIVITY_PRIORITIZATION
- Stale opportunity detection (open opp, no recent activity within cadence window)
- Cadence recommendation — when to follow up next based on stage, close date, last touch
- Follow-up email draft using EMAIL_LIBRARY templates and EMAIL_STYLE_GUIDE
- Objection-aware follow-up framing when last activity notes mention blocker (CUSTOMER_OBJECTION_LIBRARY)
- "What follow-ups am I behind on?" — user-scoped overdue + stale rollup
- Single activity or opp drill-down with suggested_message and recommended_timing

## Playbook / Library Usage

| Library | Application |
|---------|-------------|
| ACTIVITY_PRIORITIZATION | Revenue-critical overdue first, then SLA commitments, then hygiene |
| EMAIL_LIBRARY | Follow-up after meeting, re-engagement, case-adjacent sales touch |
| CUSTOMER_OBJECTION_LIBRARY | Tailor suggested_message when objection noted in activity/opp |

## Cadence Defaults (Layer 4 overridable)

| Stage / Context | Suggested max days without activity |
|-----------------|-------------------------------------|
| Negotiation / Commit | 3 |
| Proposal / Solution | 5 |
| Discovery / Qualification | 7 |
| Early stage / Lead nurture | 14 |
| Close date ≤ 14 days | 2 (override stage default) |
