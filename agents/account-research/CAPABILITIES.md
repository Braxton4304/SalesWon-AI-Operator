# Capabilities

What this agent **is allowed** to do. Aligns with [data-spec](../../specifications/data-spec.md) permissions.

## Read

| Object | Use Cases |
|--------|-----------|
| **Account** | Tier, industry, parent/child hierarchy, strategic value, open opps and cases |
| **Contact** | Stakeholder roles, reporting relationships, engagement recency |
| **Opportunity** | Pipeline context, stage, amount, close dates, competitors, linked contacts |
| **Case** | Service health, P1/P2 patterns, sentiment signals, renewal risk |
| **Activity** | Recent engagement history, meeting cadence, overdue follow-ups |

## Response Types

- **Account brief** — Executive snapshot per ACCOUNT_PLANNING and EXECUTIVE_SUMMARY_STANDARD
- **Relationship map** — Contacts with inferred roles (economic buyer, champion, blocker, influencer)
- **Opportunity context** — Open pipeline summary for the account
- **Service context** — Open cases, SLA posture, risk signals per CUSTOMER_RISK_GUIDE
- **Buying signals** — CRM-derived indicators (new opp, stage progression, budget cycle, expansion)
- **Risk assessment** — Customer and deal risks with severity
- **Meeting prep** — Attendee brief, agenda suggestions, last activities per MEETING_PREPARATION
- **Research questions** — SPIN-aligned discovery questions per DISCOVERY_PLAYBOOK
- **White-space analysis** — Products not purchased vs. installed base (when CRM data available)

## Draft-Only (recommend)

| Object | Draft Types |
|--------|-------------|
| **Activity** | Meeting prep task, research follow-up task for rep |
| **Opportunity** | Discovery notes summary (rep commits) |

Account object is **read-only** (writable: none per data-spec). Account plan field updates are recommendations in narrative form only.

## Shared Knowledge

| Playbook | Chapters / Sections Used |
|----------|--------------------------|
| DISCOVERY_PLAYBOOK | SPIN framework, discovery questions, CRM documentation |
| ACCOUNT_PLANNING | Tier, white-space, relationship map, 90-day objectives |
| CUSTOMER_RISK_GUIDE | Risk signals, case + opp correlation |
| MEETING_PREPARATION | Brief structure, attendee roles, agenda |

## Tools

See [TOOLS.md](TOOLS.md).
