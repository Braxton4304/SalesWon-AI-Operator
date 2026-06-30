# Reasoning Patterns

Agent-specific reasoning chains. Maps to [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) actions.

## Pattern 1: Full Team Pipeline Review

```text
Input (team scope + period)
  → Step 1: Resolve team scope (query_team_pipeline) — ask if ambiguous
  → Step 2: Gather team opps (query_opportunities) → stage + forecast distribution
  → Step 3: Gather activities (query_activities) → recency per opp
  → Step 4: Apply PIPELINE_HEALTH_MODEL → health per opp
  → Step 5: Apply PIPELINE_INSPECTION_GUIDE checklist → hygiene flags
  → Step 6: Compute DECISION_MODEL priority_score → rank forecast_risks
  → Step 7: Select top_intervention_opportunities (top N by score)
  → Step 8: Generate rep_coaching_items per rep patterns
  → Step 9: Assemble pipeline_summary + manager_actions
  → Step 10: Compute confidence → missing_data → decision_action answer | escalate
```

## Pattern 2: Forecast Risk Focus (Time Window)

```text
Input (close_date window + forecast category filter)
  → Step 1: query_opportunities (filter close_date + forecast_category)
  → Step 2: query_activities (recency on filtered opps)
  → Step 3: query_cases (accounts with commit opps) → service_risk signal
  → Step 4: Score health + priority_score
  → Step 5: forecast_risks + top_intervention_opportunities primary
  → Step 6: pipeline_summary condensed; rep_coaching_items for affected reps
  → Step 7: answer
```

## Pattern 3: Rep Coaching Session Prep

```text
Input (named rep)
  → Step 1: query_opportunities (owner filter)
  → Step 2: query_activities (rep + opp recency)
  → Step 3: PIPELINE_INSPECTION_GUIDE per rep opp
  → Step 4: rep_coaching_items (constructive, balanced with wins)
  → Step 5: forecast_risks subset for rep's opps
  → Step 6: manager_actions for 1:1 agenda
  → Step 7: answer — coaching primary; pipeline_summary metrics condensed
```

## Pattern 4: Executive Forecast Brief

```text
Input (exec brief + meeting date)
  → Step 1: Pattern 1 full pipeline review
  → Step 2: Assemble executive_brief per EXECUTIVE_SUMMARY_STANDARD
  → Step 3: Headline + 3–5 metrics + highlights + risks + actions
  → Step 4: Elevate completeness if meeting within 7 days
  → Step 5: manager_actions aligned to brief actions section
  → Step 6: answer — executive_brief populated under pipeline_summary
```

## Pattern 5: Pipeline Hygiene Sprint

```text
Input (hygiene focus + forecast category)
  → Step 1: query_opportunities (forecast category filter)
  → Step 2: PIPELINE_INSPECTION_GUIDE required field checks
  → Step 3: data_hygiene_issues array with checklist_item
  → Step 4: manager_actions — hygiene sprint with owners and due date
  → Step 5: answer — hygiene primary; forecast_risks for affected opps only
```

## Pattern 6: Strategic Account Forecast Review

```text
Input (account name + forecast context)
  → Step 1: query_accounts + query_opportunities (account filter)
  → Step 2: Optional: user-provided account_brief from Account Research
  → Step 3: query_cases → service_risk on forecast opps
  → Step 4: forecast_risks for account opps with strategic weighting
  → Step 5: rep_coaching_items + manager_actions for account
  → Step 6: answer
```

## Decision Engine Mapping

| Step Outcome | decision_action |
|--------------|-----------------|
| Team scope not found | ask or retrieve |
| Multiple team matches | ask |
| Required data missing after 3 retrieves | escalate |
| Forecast commit request | refuse |
| Territory reassignment request | refuse |
| Sufficient CRM context | answer |
| Manager action plan appropriate | recommend (draft agenda) |

```yaml
reasoning_version: "1.0.0"
agent_id: sales-manager
patterns:
  - full_team_pipeline_review
  - forecast_risk_focus
  - rep_coaching_prep
  - executive_forecast_brief
  - pipeline_hygiene_sprint
  - strategic_account_forecast_review
```
