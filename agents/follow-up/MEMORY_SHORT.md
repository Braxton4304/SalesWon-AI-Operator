# Short Memory

- Active activity sys_id(s) and overdue list context from current session
- Opportunity being followed up (sys_id, name) when user drills into a deal
- Email draft iteration state (subject/body versions user asked to refine)
- Cadence window overrides user stated ("I'm out until Friday")
- Last ranked overdue list hash — re-query if user may have completed tasks in ServiceNow

## Task States

`overdue_review`, `cadence_planning`, `drafting_email`, `stale_opp_recovery`, `objection_follow_up`

## Session Boundaries

Clear overdue cache when user switches assignee scope or says "refresh my list."
