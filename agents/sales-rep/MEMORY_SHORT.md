# Short Memory

Session-scoped context for multi-turn rep conversations. Re-query CRM when user may have updated records mid-session.

## Retained Context

- Active opportunity sys_id(s) and names
- Meeting prep context (attendees, date) if scheduling discussion
- Draft email iteration state (suggested_follow_up revisions)
- Qualification checklist progress for current deal (MEDDIC/SPIN/Sandler gaps addressed)
- Last DECISION_MODEL priority_score for active opp (hint only — recompute on refresh)
- Pipeline planning scope (today / this week / named filter)

## Task States

`deal_review`, `meeting_prep`, `drafting_email`, `pipeline_planning`, `objection_coaching`, `discovery_coaching`, `qualification_audit`

## Refresh Rules

- Re-query opportunity when user mentions CRM update, stage change, or new activity
- Clear draft iteration state when suggested_follow_up accepted or rejected
- Do not cache financials across sessions — always source from source_records on output
- Pipeline totals in memory are hints only — always re-query for final OUTPUT_SCHEMA

## Memory Boundaries

- No cross-rep pipeline data in session memory
- No manager coaching items unless user pasted in current session
- account_brief from Account Research Agent held as user-provided context only — not authoritative CRM

```yaml
memory_short_version: "1.1.0"
agent_id: sales-rep
scope: session
authoritative_source: crm_requery
```
