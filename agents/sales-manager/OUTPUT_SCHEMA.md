# Output Schema

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

Every response MUST validate against this schema.

## Processing Pipeline

```text
Input
  │
  ├─ Parse manager request (team scope, period, rep filter, brief type)
  ├─ Resolve visibility boundary (manager-scoped team pipeline view)
  └─ decision_action: ask if team/rep/period ambiguous
  │
Processing
  │
  ├─ Retrieve: query_team_pipeline → query_opportunities → query_activities
  ├─ Optional: query_cases for forecast-risk accounts (CUSTOMER_RISK_GUIDE)
  ├─ Apply PIPELINE_INSPECTION_GUIDE checklist per opp
  ├─ Score health per PIPELINE_HEALTH_MODEL (5 signals)
  ├─ Compute priority_score per DECISION_MODEL (weights sum 100%)
  ├─ Rank top_intervention_opportunities and forecast_risks
  ├─ Generate rep_coaching_items (constructive, evidence-linked)
  ├─ Flag data_hygiene_issues on missing required fields
  ├─ Assemble pipeline_summary + EXECUTIVE_SUMMARY_STANDARD executive_brief
  └─ Propose manager_actions (recommend only — human executes)
  │
Output
  │
  ├─ SalesManagerAgentOutput JSON (all required fields)
  ├─ summary: human-readable manager headline
  └─ source_records: field-level audit trail
  │
Confidence
  │
  ├─ Compute per TRUST_MODEL factor table
  ├─ Reduce for missing quota, incomplete opp fields, stale team view
  └─ Band: high ≥0.85 | medium 0.60–0.84 | low <0.60
  │
Escalation
  │
  ├─ confidence < 0.60 after 3 retrieves → decision_action: escalate
  ├─ forecast commit / territory change request → refuse
  └─ Include escalation_payload per ESCALATION.md when escalating
  │
Audit
  │
  ├─ Log tool calls, decision_action, confidence, sources
  ├─ source_records authoritative for factual assertions
  └─ Persist per governance-spec audit record
```

## Machine-Readable Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "SalesManagerAgentOutput",
  "type": "object",
  "required": [
    "summary",
    "confidence",
    "sources",
    "decision_action",
    "pipeline_summary",
    "forecast_risks",
    "top_intervention_opportunities",
    "rep_coaching_items",
    "data_hygiene_issues",
    "manager_actions",
    "missing_data",
    "source_records"
  ],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Manager-facing headline — pipeline posture or exec decision needed"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Overall response confidence per TRUST_MODEL"
    },
    "sources": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "id"],
        "properties": {
          "type": { "enum": ["crm", "kb", "policy"] },
          "id": { "type": "string" },
          "label": { "type": "string" }
        }
      }
    },
    "decision_action": {
      "enum": ["answer", "ask", "retrieve", "escalate", "refuse", "recommend"]
    },
    "pipeline_summary": {
      "type": "object",
      "required": ["headline", "period", "metrics"],
      "properties": {
        "headline": { "type": "string" },
        "period": { "type": "string" },
        "team_scope": { "type": "string" },
        "metrics": {
          "type": "object",
          "properties": {
            "weighted_pipeline": { "type": "number" },
            "unweighted_pipeline": { "type": "number" },
            "quota": { "type": ["number", "null"] },
            "coverage_ratio": { "type": ["number", "null"] },
            "commit_pipeline": { "type": "number" },
            "best_case_pipeline": { "type": "number" },
            "open_opportunity_count": { "type": "integer" },
            "at_risk_count": { "type": "integer" },
            "critical_count": { "type": "integer" },
            "hygiene_issue_count": { "type": "integer" }
          }
        },
        "stage_distribution": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "stage": { "type": "string" },
              "count": { "type": "integer" },
              "weighted_amount": { "type": "number" }
            }
          }
        },
        "forecast_category_distribution": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "category": { "enum": ["commit", "best_case", "pipeline", "omitted"] },
              "count": { "type": "integer" },
              "weighted_amount": { "type": "number" }
            }
          }
        },
        "highlights": {
          "type": "array",
          "items": { "type": "string" }
        },
        "executive_brief": {
          "type": "object",
          "description": "EXECUTIVE_SUMMARY_STANDARD structure when brief requested",
          "properties": {
            "headline": { "type": "string" },
            "metrics": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "label": { "type": "string" },
                  "value": { "type": "string" },
                  "comparison": { "type": "string" }
                }
              }
            },
            "highlights": { "type": "array", "items": { "type": "string" } },
            "risks": { "type": "array", "items": { "type": "string" } },
            "actions": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },
    "forecast_risks": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["opportunity_id", "name", "severity", "health", "signals", "priority_score"],
        "properties": {
          "opportunity_id": { "type": "string" },
          "name": { "type": "string" },
          "owner": { "type": "string" },
          "amount": { "type": "number" },
          "stage": { "type": "string" },
          "forecast_category": { "enum": ["commit", "best_case", "pipeline", "omitted"] },
          "close_date": { "type": "string", "format": "date" },
          "health": { "enum": ["healthy", "at_risk", "critical", "unknown"] },
          "severity": { "enum": ["critical", "high", "medium", "low"] },
          "signals": {
            "type": "array",
            "items": {
              "enum": [
                "stage_velocity",
                "close_date_slip",
                "activity_recency",
                "amount_probability_gap",
                "threading",
                "service_risk"
              ]
            }
          },
          "priority_score": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "DECISION_MODEL weighted score"
          },
          "intervention_rationale": { "type": "string" },
          "days_to_close": { "type": "integer" },
          "days_since_activity": { "type": "integer" }
        }
      }
    },
    "top_intervention_opportunities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["opportunity_id", "name", "priority_score", "recommended_intervention"],
        "properties": {
          "opportunity_id": { "type": "string" },
          "name": { "type": "string" },
          "owner": { "type": "string" },
          "amount": { "type": "number" },
          "priority_score": { "type": "number" },
          "recommended_intervention": { "type": "string" },
          "urgency": { "enum": ["immediate", "this_week", "this_month", "monitor"] }
        }
      }
    },
    "rep_coaching_items": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["rep_name", "topic", "evidence", "suggested_action"],
        "properties": {
          "rep_name": { "type": "string" },
          "rep_id": { "type": "string" },
          "topic": { "type": "string" },
          "coaching_type": {
            "enum": ["pipeline_review", "activity_cadence", "forecast_hygiene", "deal_strategy", "positive_recognition"]
          },
          "evidence": { "type": "string" },
          "linked_opportunity_ids": {
            "type": "array",
            "items": { "type": "string" }
          },
          "suggested_action": { "type": "string" },
          "suggested_1on1_agenda_item": { "type": "string" }
        }
      }
    },
    "data_hygiene_issues": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["opportunity_id", "missing_fields", "impact"],
        "properties": {
          "opportunity_id": { "type": "string" },
          "name": { "type": "string" },
          "owner": { "type": "string" },
          "forecast_category": { "type": "string" },
          "missing_fields": {
            "type": "array",
            "items": { "type": "string" }
          },
          "impact": { "type": "string" },
          "checklist_item": {
            "type": "string",
            "description": "PIPELINE_INSPECTION_GUIDE reference"
          }
        }
      }
    },
    "manager_actions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["action", "owner", "priority"],
        "properties": {
          "action_number": { "type": "integer" },
          "action": { "type": "string" },
          "owner": { "type": "string" },
          "priority": { "enum": ["critical", "high", "medium", "low"] },
          "due_suggestion": { "type": "string" },
          "linked_opportunity_ids": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    },
    "missing_data": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["field", "object", "impact"],
        "properties": {
          "field": { "type": "string" },
          "object": {
            "enum": ["opportunity", "account", "activity", "team_pipeline_view", "quota"]
          },
          "impact": { "type": "string" }
        }
      }
    },
    "source_records": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["object", "id"],
        "properties": {
          "object": {
            "enum": ["opportunity", "account", "activity", "case", "team_pipeline_view", "kb", "policy"]
          },
          "id": { "type": "string" },
          "label": { "type": "string" },
          "fields_used": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    },
    "recommended_action": {
      "type": "object",
      "description": "Required when decision_action is recommend",
      "properties": {
        "type": { "enum": ["pipeline_review", "rep_1on1", "forecast_call_agenda", "escalation"] },
        "target_record_id": { "type": "string" },
        "draft_payload": { "type": "object" }
      }
    },
    "clarifying_question": {
      "type": "string",
      "description": "Required when decision_action is ask"
    }
  }
}
```

## Example (Demo — Q3 Team Pipeline Review)

```json
{
  "summary": "Q3 team pipeline: $2.1M weighted ($2.8M coverage vs $750K quota). 4 commit deals at risk ($680K) — prioritize Acme Expansion and Globex Renewal before forecast call Friday.",
  "confidence": 0.91,
  "sources": [
    { "type": "crm", "id": "tpv-emea-q3", "label": "EMEA Enterprise Q3 Pipeline View" },
    { "type": "policy", "id": "pipeline_health_model", "label": "PIPELINE_HEALTH_MODEL" },
    { "type": "policy", "id": "pipeline_inspection_guide", "label": "PIPELINE_INSPECTION_GUIDE" }
  ],
  "decision_action": "answer",
  "pipeline_summary": {
    "headline": "Coverage strong at 2.8× but commit bucket carries $680K at-risk exposure in next 30 days",
    "period": "Q3 FY26",
    "team_scope": "EMEA Enterprise",
    "metrics": {
      "weighted_pipeline": 2100000,
      "unweighted_pipeline": 2650000,
      "quota": 750000,
      "coverage_ratio": 2.8,
      "commit_pipeline": 920000,
      "best_case_pipeline": 680000,
      "open_opportunity_count": 24,
      "at_risk_count": 6,
      "critical_count": 2,
      "hygiene_issue_count": 5
    },
    "stage_distribution": [
      { "stage": "Discovery", "count": 8, "weighted_amount": 320000 },
      { "stage": "Proposal", "count": 9, "weighted_amount": 980000 },
      { "stage": "Negotiation", "count": 7, "weighted_amount": 800000 }
    ],
    "forecast_category_distribution": [
      { "category": "commit", "count": 11, "weighted_amount": 920000 },
      { "category": "best_case", "count": 7, "weighted_amount": 680000 },
      { "category": "pipeline", "count": 6, "weighted_amount": 500000 }
    ],
    "highlights": [
      "Northwind Traders closed-won $185K — Jordan Lee",
      "Contoso upsell advanced to Negotiation within 21 days — Alex Rivera"
    ],
    "executive_brief": {
      "headline": "Q3 forecast achievable with intervention on 4 commit at-risk deals before month-end",
      "metrics": [
        { "label": "Weighted Pipeline", "value": "$2.1M", "comparison": "vs $1.9M prior quarter" },
        { "label": "Coverage Ratio", "value": "2.8×", "comparison": "quota $750K" },
        { "label": "Commit Pipeline", "value": "$920K", "comparison": "74% at or ahead of plan" },
        { "label": "At-Risk Commit", "value": "$680K", "comparison": "4 deals — 74% of commit risk" },
        { "label": "Hygiene Issues", "value": "5 opps", "comparison": "commit category" }
      ],
      "highlights": [
        "Northwind $185K closed-won this period",
        "Contoso upsell on track for Negotiation close"
      ],
      "risks": [
        "Acme Expansion: 19 days no activity, P2 case open, close 2026-07-15",
        "Globex Renewal: close date slipped once, single-threaded",
        "Fabrikam deal: probability 80% at Discovery stage — misaligned"
      ],
      "actions": [
        "Manager 1:1 with Jordan Lee on Acme + Globex commit deals — this week",
        "Pipeline hygiene sprint on 5 commit opps missing required fields — by Wednesday",
        "Executive sponsor review for Acme CIO engagement gap — before 2026-07-10"
      ]
    }
  },
  "forecast_risks": [
    {
      "opportunity_id": "opp789",
      "name": "Acme Expansion FY26",
      "owner": "Jordan Lee",
      "amount": 250000,
      "stage": "Proposal",
      "forecast_category": "commit",
      "close_date": "2026-07-15",
      "health": "at_risk",
      "severity": "high",
      "signals": ["activity_recency", "close_date_slip", "service_risk"],
      "priority_score": 0.78,
      "intervention_rationale": "Commit deal closing in 15 days with 19 days since last activity; P2 integration case open on account per CUSTOMER_RISK_GUIDE",
      "days_to_close": 15,
      "days_since_activity": 19
    },
    {
      "opportunity_id": "opp321",
      "name": "Globex Platform Renewal",
      "owner": "Jordan Lee",
      "amount": 180000,
      "stage": "Negotiation",
      "forecast_category": "commit",
      "close_date": "2026-07-22",
      "health": "at_risk",
      "severity": "high",
      "signals": ["close_date_slip", "threading"],
      "priority_score": 0.72,
      "intervention_rationale": "Close date slipped once; single contact on late-stage renewal",
      "days_to_close": 22,
      "days_since_activity": 12
    },
    {
      "opportunity_id": "opp445",
      "name": "Fabrikam New Platform",
      "owner": "Alex Rivera",
      "amount": 95000,
      "stage": "Discovery",
      "forecast_category": "commit",
      "close_date": "2026-07-28",
      "health": "critical",
      "severity": "critical",
      "signals": ["amount_probability_gap", "stage_velocity"],
      "priority_score": 0.81,
      "intervention_rationale": "80% probability at Discovery stage — forecast category not justified per PIPELINE_INSPECTION_GUIDE",
      "days_to_close": 28,
      "days_since_activity": 8
    }
  ],
  "top_intervention_opportunities": [
    {
      "opportunity_id": "opp445",
      "name": "Fabrikam New Platform",
      "owner": "Alex Rivera",
      "amount": 95000,
      "priority_score": 0.81,
      "recommended_intervention": "Immediate forecast category review — downgrade or advance stage with evidence",
      "urgency": "immediate"
    },
    {
      "opportunity_id": "opp789",
      "name": "Acme Expansion FY26",
      "owner": "Jordan Lee",
      "amount": 250000,
      "priority_score": 0.78,
      "recommended_intervention": "Manager-led exec alignment session; resolve P2 case before forecast commit",
      "urgency": "this_week"
    },
    {
      "opportunity_id": "opp321",
      "name": "Globex Platform Renewal",
      "owner": "Jordan Lee",
      "amount": 180000,
      "priority_score": 0.72,
      "recommended_intervention": "Multi-thread renewal — identify economic buyer and secondary contact",
      "urgency": "this_week"
    }
  ],
  "rep_coaching_items": [
    {
      "rep_name": "Jordan Lee",
      "rep_id": "rep-jordan",
      "topic": "Commit deal activity cadence",
      "coaching_type": "activity_cadence",
      "evidence": "2 commit opps ($430K combined) with 12–19 days since last logged activity",
      "linked_opportunity_ids": ["opp789", "opp321"],
      "suggested_action": "Establish weekly activity plan for Acme and Globex with dated next steps in CRM",
      "suggested_1on1_agenda_item": "Review activity plan for commit deals closing in July"
    },
    {
      "rep_name": "Alex Rivera",
      "rep_id": "rep-alex",
      "topic": "Forecast category discipline",
      "coaching_type": "forecast_hygiene",
      "evidence": "Fabrikam opp at Discovery with 80% probability in commit category",
      "linked_opportunity_ids": ["opp445"],
      "suggested_action": "Reconcile stage/probability with manager before forecast call",
      "suggested_1on1_agenda_item": "Walk through Fabrikam qualification criteria and forecast justification"
    },
    {
      "rep_name": "Jordan Lee",
      "rep_id": "rep-jordan",
      "topic": "Positive recognition",
      "coaching_type": "positive_recognition",
      "evidence": "Northwind Traders $185K closed-won this period",
      "linked_opportunity_ids": ["opp112"],
      "suggested_action": "Highlight win in team meeting; capture winning pattern for playbook",
      "suggested_1on1_agenda_item": "What worked on Northwind — replicate on similar accounts"
    }
  ],
  "data_hygiene_issues": [
    {
      "opportunity_id": "opp789",
      "name": "Acme Expansion FY26",
      "owner": "Jordan Lee",
      "forecast_category": "commit",
      "missing_fields": ["next_step"],
      "impact": "Cannot verify rep activity plan for commit deal inspection",
      "checklist_item": "Required opp fields complete (amount, probability, close_date, owner)"
    },
    {
      "opportunity_id": "opp321",
      "name": "Globex Platform Renewal",
      "owner": "Jordan Lee",
      "forecast_category": "commit",
      "missing_fields": ["secondary_contact"],
      "impact": "Multi-threading check fails — single-threaded flag",
      "checklist_item": "Multi-threading (2+ contacts on late stage)"
    },
    {
      "opportunity_id": "opp445",
      "name": "Fabrikam New Platform",
      "owner": "Alex Rivera",
      "forecast_category": "commit",
      "missing_fields": ["forecast_category_justification"],
      "impact": "Commit category not aligned to Discovery stage",
      "checklist_item": "Forecast category justified"
    }
  ],
  "manager_actions": [
    {
      "action_number": 1,
      "action": "Schedule 1:1 with Jordan Lee focused on Acme Expansion and Globex Renewal activity plans",
      "owner": "Manager",
      "priority": "high",
      "due_suggestion": "This week",
      "linked_opportunity_ids": ["opp789", "opp321"]
    },
    {
      "action_number": 2,
      "action": "Facilitate forecast category review for Fabrikam with Alex Rivera before Friday forecast call",
      "owner": "Manager",
      "priority": "critical",
      "due_suggestion": "Before 2026-07-04",
      "linked_opportunity_ids": ["opp445"]
    },
    {
      "action_number": 3,
      "action": "Assign hygiene sprint: 5 commit opps missing required fields — reps update CRM by Wednesday",
      "owner": "Jordan Lee, Alex Rivera",
      "priority": "medium",
      "due_suggestion": "2026-07-02",
      "linked_opportunity_ids": ["opp789", "opp321", "opp445"]
    },
    {
      "action_number": 4,
      "action": "Escalate Acme P2 integration case with CS leadership before forecast commit decision",
      "owner": "Manager + CS Lead",
      "priority": "high",
      "due_suggestion": "Before 2026-07-10",
      "linked_opportunity_ids": ["opp789"]
    }
  ],
  "missing_data": [],
  "source_records": [
    { "object": "team_pipeline_view", "id": "tpv-emea-q3", "label": "EMEA Enterprise Q3", "fields_used": ["weighted_pipeline", "quota", "period"] },
    { "object": "opportunity", "id": "opp789", "label": "Acme Expansion FY26", "fields_used": ["amount", "stage", "close_date", "forecast_category", "probability"] },
    { "object": "opportunity", "id": "opp321", "label": "Globex Platform Renewal", "fields_used": ["amount", "close_date", "owner"] },
    { "object": "opportunity", "id": "opp445", "label": "Fabrikam New Platform", "fields_used": ["stage", "probability", "forecast_category"] },
    { "object": "activity", "id": "act550", "label": "Last Acme activity", "fields_used": ["completed_date"] },
    { "object": "case", "id": "cs2001", "label": "Acme P2 integration", "fields_used": ["priority", "state"] },
    { "object": "policy", "id": "pipeline_health_model", "label": "PIPELINE_HEALTH_MODEL", "fields_used": ["signals"] }
  ]
}
```

## Field Notes

- `confidence` reflects overall response quality per [TRUST_MODEL.md](TRUST_MODEL.md)
- Empty arrays are valid when no risks/coaching/hygiene exist — do not omit required arrays
- `coverage_ratio` is null when quota unavailable — list in missing_data
- `priority_score` uses DECISION_MODEL weights summing to 100%
- `executive_brief` nested under `pipeline_summary` when user requests exec/forecast brief
- `source_records` is the authoritative audit trail; `sources` remains for runtime compatibility

```yaml
output_schema_version: "1.0.0"
agent_id: sales-manager
primary_artifacts: [pipeline_summary, rep_coaching_items]
pipeline_stages: [input, processing, output, confidence, escalation, audit]
```
