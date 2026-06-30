# Tools

Implements: [specifications/data-spec.md](../../specifications/data-spec.md), [AUTHORITY.md](AUTHORITY.md)

## query_opportunity

Retrieve opp by number/sys_id with account, contacts, stage, financials.

**Required fields check:** amount, probability, close_date, owner

**Precondition:** Always call before deal assertions or opportunity_summary population.

## query_pipeline

List open opportunities for authenticated user with filters (stage, close_date range, amount min).

**Use:** "What should I do today?" — input to DECISION_MODEL ranking.

## query_account

Account profile with linked opps, contacts, recent cases (read-only context).

**Use:** Meeting prep, stakeholder context, service risk on active deal.

## query_activities

Activities for opportunity or account; highlight overdue.

**Use:** Activity recency gap factor (15% weight), deal_health scoring.

## query_lead

Lead record for SDR workflows.

**Use:** Early-stage SPIN/Sandler qualification before opp conversion.

## query_contacts

Stakeholders linked to opp/account with role labels.

**Use:** MEDDIC economic_buyer and champion gap detection.

## retrieve_knowledge

Product docs, playbook excerpts, battlecards, methodology guides (RAG).

**Use:** Objection handling, recommended_questions templates, product capability bounds.

## draft_opportunity_update

Propose next_step, stage, description updates — draft_only.

**Authority:** draft → recommend per AUTHORITY.md.

## draft_activity

Propose call, email task, meeting with due_date.

**Use:** suggested_follow_up when type is activity_task.

## draft_email

Customer/prospect email draft linked to opp/contact.

**Use:** suggested_follow_up when type is email_draft; follows EMAIL_STYLE_GUIDE.

## Tool Chain Patterns

```text
Deal review:
  query_opportunity → query_activities → query_contacts → MEDDIC gap scan → DECISION_MODEL score

Pipeline today:
  query_pipeline → query_activities (batch) → rank by priority_score → next_best_action per opp

Meeting prep:
  query_opportunity → query_account → query_contacts → query_activities → opportunity_summary

Discovery coaching:
  query_opportunity → query_lead (if pre-opp) → SPIN recommended_questions
```

## Rules

1. query_opportunity before deal assertions
2. Rank "today" lists using DECISION_MODEL weighted formula (weights sum 100%)
3. No autonomous send — all writes via draft → recommend
4. Log all tool calls in source_records audit trail
5. Up to 3 retrieve cycles before escalate on low confidence

```yaml
tools_version: "1.1.0"
agent_id: sales-rep
write_mode: draft_only
autonomous_send: false
```
