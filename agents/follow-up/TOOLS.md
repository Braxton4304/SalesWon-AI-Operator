# Tools

## query_activities

Retrieve activities for user, opportunity, or account with filters (state, due_date range, type).

**Overdue filter:** `due_date < today AND state NOT IN (Closed, Complete, Cancelled)`

## query_overdue_activities

Shortcut for authenticated user's open overdue activities, sorted by DECISION_MODEL priority_score.

## query_opportunity

Linked opportunity for stage, amount, probability, close_date, next_step — used for revenue weighting.

## query_account

Account context for tier and strategic cadence adjustments.

## query_contact

Recipient name, email, role for email drafts.

## detect_stale_opportunities

Open opps for user where last completed activity exceeds stage cadence window (CAPABILITIES defaults).

## retrieve_knowledge

EMAIL_LIBRARY excerpts, objection responses, product value statements (RAG).

## draft_activity

Propose follow-up task with due_date, type, description — draft_only.

## draft_email

Customer email draft using EMAIL_STYLE_GUIDE; links to activity_id and/or opportunity_id.

**draft_payload:** subject, body, suggested_send_window

## Rules

1. query_activities or query_overdue_activities before asserting overdue status
2. query_opportunity before revenue-weighted priority when opp linked
3. draft_email requires contact email from CRM or explicit user input
4. No tool may send or transition activity to Complete
5. Rank lists using ACTIVITY_PRIORITIZATION stack: revenue-critical → SLA → relationship → hygiene

## Tool → Output Field Mapping

| Tool result | Populates |
|-------------|-----------|
| query_overdue_activities | related_activity, source_records |
| query_opportunity | related_opportunity |
| draft_email | suggested_message, recommended_action.draft_payload |
| detect_stale_opportunities | reason (stale cadence), related_opportunity |
