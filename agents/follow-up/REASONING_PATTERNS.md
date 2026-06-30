# Reasoning Patterns

Maps follow-up decisions to [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) actions.

## Chain A — Overdue Activity List

```text
Input (user: "What's overdue?")
  → Step 1: Authenticate user scope [RUNTIME_CONTEXT]
  → Step 2: query_overdue_activities [retrieve]
  → Step 3: Enrich linked opportunities [retrieve]
  → Step 4: Compute priority_score per DECISION_MODEL [analyze]
  → Step 5: Map to follow_up_priority labels [analyze]
  → Step 6: Build source_records + summary [answer/recommend]
  → Confidence: high if due_date + state present on all items
  → Escalate? No unless strategic account critical list match
```

## Chain B — Single Follow-Up with Email Draft

```text
Input (activity or opp identifier)
  → Step 1: query_activities / query_opportunity [retrieve]
  → Step 2: Validate overdue or stale cadence [analyze]
  → Step 3: query_contact for recipient [retrieve]
  → Step 4: Check activity notes for objections [analyze]
  → Step 5: Select EMAIL_LIBRARY template [analyze]
  → Step 6: draft_email → suggested_message [recommend]
  → Step 7: Set recommended_timing from cadence rules [recommend]
  → Confidence: medium-high; reduce if contact email missing
  → Escalate? If objection = pricing → escalation_required
```

## Chain C — Cadence Timing Only

```text
Input ("When should I follow up on X?")
  → Step 1: query_opportunity + query_activities [retrieve]
  → Step 2: Last completed activity date vs stage cadence [analyze]
  → Step 3: close_date proximity override [analyze]
  → Step 4: recommended_timing + reason [answer]
  → Confidence: high with last_activity_date; ask if none found
  → Escalate? No
```

## Chain D — Stale Opportunity (No Overdue Task)

```text
Input (opp name/number)
  → Step 1: query_opportunity [retrieve]
  → Step 2: detect_stale_opportunities logic [analyze]
  → Step 3: ACTIVITY_PRIORITIZATION revenue weight [analyze]
  → Step 4: Re-engagement suggested_message [recommend]
  → Confidence: reduce if last_activity_date ambiguous
  → Escalate? If amount > threshold + close ≤ 14d → manager notify
```

## Decision Engine Mapping

| Step type | DECISION_ENGINE action |
|-----------|------------------------|
| CRM fetch | retrieve |
| Overdue/stale math | analyze |
| Draft generation | recommend |
| Missing required field | ask |
| Pricing/legal trigger | escalate |
| Out of scope request | refuse + handoff hint |

```yaml
reasoning_patterns_version: "1.0.0"
agent_id: follow-up
primary_chains: [overdue_list, email_draft, cadence_timing, stale_opp]
```
