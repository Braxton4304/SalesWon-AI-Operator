# Reasoning Patterns

Agent-specific reasoning chains. Maps to [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) actions.

## Pattern 1: Single Opportunity Deal Review

```text
Input (opp name/ID)
  → Step 1: Resolve opp (query_opportunity) — ask if ambiguous
  → Step 2: Gather activities (query_activities) → days_since_activity
  → Step 3: Gather contacts (query_contacts) → MEDDIC role mapping
  → Step 4: Apply MEDDIC/SPIN/Sandler gap analysis → qualification_gaps
  → Step 5: Score deal_health per PIPELINE_HEALTH_MODEL
  → Step 6: Compute DECISION_MODEL priority_score → next_best_action
  → Step 7: Generate recommended_questions for blocking gaps
  → Step 8: Assemble opportunity_summary + source_records
  → Step 9: Propose suggested_follow_up if action is email/meeting
  → Step 10: Compute confidence → missing_data → escalation_required → answer | escalate
```

## Pattern 2: Pipeline Prioritization ("What Should I Do Today?")

```text
Input (rep pipeline scope)
  → Step 1: query_pipeline (open opps for authenticated user)
  → Step 2: query_activities (batch recency per opp)
  → Step 3: Lightweight MEDDIC gap scan per opp
  → Step 4: Compute priority_score per DECISION_MODEL for each opp
  → Step 5: Rank pipeline_rankings (top N by score)
  → Step 6: Full OUTPUT_SCHEMA for top opp; condensed for others
  → Step 7: next_best_action for #1 ranked opp
  → Step 8: answer — pipeline_rankings primary
```

## Pattern 3: Meeting Prep

```text
Input (opp + meeting date + optional attendees)
  → Step 1: query_opportunity + query_account
  → Step 2: Optional: user-provided account_brief from Account Research
  → Step 3: query_contacts (attendees + stakeholders)
  → Step 4: query_activities (recent engagement summary)
  → Step 5: opportunity_summary with meeting context
  → Step 6: recommended_questions (SPIN discovery + MEDDIC validation)
  → Step 7: suggested_follow_up (meeting agenda or pre-meeting email draft)
  → Step 8: answer
```

## Pattern 4: Discovery / Early-Stage Qualification

```text
Input (lead or early-stage opp)
  → Step 1: query_lead or query_opportunity
  → Step 2: Sandler upfront contract + pain funnel check
  → Step 3: SPIN recommended_questions (Situation, Problem, Implication, Need-payoff)
  → Step 4: qualification_gaps with SPIN/Sandler methodology tags
  → Step 5: next_best_action (discovery call or qualification meeting)
  → Step 6: deal_health (often at_risk if pain undocumented)
  → Step 7: answer — recommended_questions primary
```

## Pattern 5: Objection Handling

```text
Input (objection type + opp context)
  → Step 1: query_opportunity for deal context
  → Step 2: retrieve_knowledge (playbook ch. 5, battlecards)
  → Step 3: If pricing/discount objection → refuse + escalation_required
  → Step 4: Else: next_best_action with playbook talking points
  → Step 5: recommended_questions to re-qualify (MEDDIC pain/decision)
  → Step 6: suggested_follow_up (response email draft if appropriate)
  → Step 7: answer or refuse
```

## Pattern 6: Qualification Audit (Full MEDDIC)

```text
Input (opp + "full qualification audit")
  → Step 1: Pattern 1 steps 1–3
  → Step 2: Full MEDDIC checklist — all six elements
  → Step 3: Sandler budget/decision checks for Proposal+ stage
  → Step 4: qualification_gaps with all severities (blocking first)
  → Step 5: recommended_questions per blocking gap
  → Step 6: next_best_action targeting highest-severity gap
  → Step 7: answer — qualification_gaps primary
```

## Pattern 7: Manager Coaching Integration

```text
Input (opp + user-provided rep_coaching_items from manager 1:1)
  → Step 1: Pattern 1 deal review
  → Step 2: Reconcile manager coaching with DECISION_MODEL ranking
  → Step 3: If conflict → note manager guidance in summary; defer priority
  → Step 4: next_best_action aligned to coaching when evidence supports
  → Step 5: answer
```

## Decision Engine Mapping

| Step Outcome | decision_action |
|--------------|-----------------|
| Opp not found | ask or retrieve |
| Multiple opp matches | ask |
| Required data missing after 3 retrieves | escalate |
| Pricing/discount request | refuse + escalation_required |
| Sufficient CRM context | answer |
| Draft email/activity appropriate | recommend |
| External market research request | refuse — route to Account Research |

```yaml
reasoning_version: "1.1.0"
agent_id: sales-rep
patterns:
  - single_opportunity_deal_review
  - pipeline_prioritization
  - meeting_prep
  - discovery_qualification
  - objection_handling
  - qualification_audit
  - manager_coaching_integration
methodologies: [meddic, spin, sandler]
```
