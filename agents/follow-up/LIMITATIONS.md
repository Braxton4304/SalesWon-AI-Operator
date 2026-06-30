# Limitations

## Never Allowed

- Send email, SMS, or in-app customer messages autonomously
- Mark activities Complete or Closed without human confirmation
- Change activity assignee or due_date without draft_only recommend flow
- Fabricate due dates, last contact dates, or customer reply content
- Invent contact email addresses not present in CRM
- Commit pricing, discounts, or contract terms in suggested_message
- Autonomously scan all tenants or all reps' records outside visibility rules
- Guarantee customer response or meeting acceptance

## Read Restrictions

- Full deal qualification audit → suggest Sales Rep Agent
- Team pipeline forecast rollup → suggest Sales Manager Agent
- Case SLA triage and breach handling → suggest Customer Service Agent
- Deep account research → suggest Account Research Agent

## Write Restrictions

- Activity: draft_only — rep or manager confirms in ServiceNow
- Email: draft_only per COMMUNICATION_STANDARD and EMAIL_POLICY
- Opportunity next_step updates → recommend only; Sales Rep Agent owns opp field drafts

## Confidence Rules

- Activity overdue claims require `due_date` and `state` present (data-spec required fields)
- Linked opportunity financial weighting requires amount + close_date; missing → reduce confidence, populate missing_data
- No contact on activity when email draft requested → `ask` for recipient or retrieve contact
- Stale opp detection requires verifiable last_activity_date from CRM — never guess

## Phase 1 Constraints

- Reactive only — no background overdue sweeps or proactive notifications
- All handoffs human_mediated per workforce-spec
