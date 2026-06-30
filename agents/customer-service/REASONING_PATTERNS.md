# Reasoning Patterns

Agent-specific reasoning chains. Maps to [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) actions.

## Pattern 1: Full Case Triage

```text
Input (case number)
  → Step 1: query_case — ask if case number missing or ambiguous
  → Step 2: query_account + query_contact for tier and requester context
  → Step 3: Assess customer_sentiment from case text + work notes
  → Step 4: Read ITIL impact/urgency from case fields or infer with rationale
  → Step 5: Compute SLA proximity → sla_status in case_summary
  → Step 6: Apply DECISION_MODEL priority_score (35/30/15/10/10) → severity
  → Step 7: Check ESCALATION.md triggers → escalation_required + escalation_reason
  → Step 8: Assemble case_summary + source_records
  → Step 9: Compute confidence → missing_data → decision_action answer | escalate
```

## Pattern 2: Customer Response Draft

```text
Input (case number + draft request)
  → Step 1: Pattern 1 triage (condensed if case already in session)
  → Step 2: Apply CUSTOMER_SERVICE_FRAMEWORK sentiment acknowledgment rules
  → Step 3: retrieve_knowledge if resolution steps needed in draft
  → Step 4: Generate suggested_customer_response per EMAIL_STYLE_GUIDE
  → Step 5: Populate recommended_action (email_draft) with draft_payload
  → Step 6: Verify no CUSTOMER_PROMISES violations
  → Step 7: decision_action recommend — requires_human_send true
```

## Pattern 3: SLA Risk Assessment

```text
Input (case number + SLA question)
  → Step 1: query_case with include_sla true
  → Step 2: Compute sla_proximity factor (15% weight)
  → Step 3: Update severity if SLA at_risk or breached bumps score
  → Step 4: escalation_required if SLA-IMMINENT or SLA-BREACH trigger
  → Step 5: case_summary.sla_status primary output
  → Step 6: answer — suggested_customer_response null unless requested
```

## Pattern 4: Account Case List

```text
Input (account name or sys_id)
  → Step 1: query_account → query_account_cases
  → Step 2: Per-case priority_score for open cases
  → Step 3: Rank related_cases in case_summary by priority_score desc
  → Step 4: Flag MULTI-P1 if 3+ critical cases → escalation_required
  → Step 5: summary highlights top-severity cases
  → Step 6: answer
```

## Pattern 5: Escalation Decision

```text
Input ("should I escalate?" + case number)
  → Step 1: Pattern 1 full triage
  → Step 2: Evaluate all ESCALATION.md mandatory triggers
  → Step 3: Evaluate conditional triggers (VIP-SENTIMENT, ITIL-CRITICAL, etc.)
  → Step 4: Set escalation_required boolean + escalation_reason with trigger ID
  → Step 5: recommended_action.type escalation with suggested_assignee_group
  → Step 6: answer or escalate based on routing need
```

## Pattern 6: ITIL Impact/Urgency Assessment

```text
Input (case number + ITIL question)
  → Step 1: query_case — check case.impact and case.urgency fields
  → Step 2: If fields absent: infer from short_description + work notes
  → Step 3: Populate impact and urgency objects with level, rationale, source
  → Step 4: Compute priority_score → severity band
  → Step 5: Cross-check vs. case.priority — note conflicts in missing_data
  → Step 6: answer — ITIL fields primary in output
```

## Pattern 7: Refund / Billing Request

```text
Input (customer billing or refund request)
  → Step 1: query_case for context
  → Step 2: LIMITATIONS check — refuse customer commitment
  → Step 3: escalation_required true — BILLING trigger
  → Step 4: suggested_customer_response null (no unauthorized promise)
  → Step 5: decision_action refuse + escalate
```

## Decision Engine Mapping

| Step Outcome | decision_action |
|--------------|-----------------|
| Case number not found | ask or retrieve |
| Multiple case matches | ask |
| Required fields missing after 3 retrieves | escalate |
| Refund/billing authority request | refuse |
| Legal/safety keywords | escalate |
| Sufficient CRM context | answer |
| Draft appropriate | recommend |
| Mandatory escalation trigger | escalate |

```yaml
reasoning_version: "1.0.0"
agent_id: customer-service
patterns:
  - full_case_triage
  - customer_response_draft
  - sla_risk_assessment
  - account_case_list
  - escalation_decision
  - itil_impact_urgency_assessment
  - refund_billing_request
decision_model_weights: [35, 30, 15, 10, 10]
```
