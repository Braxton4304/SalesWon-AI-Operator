# Output Schema

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

Every response MUST validate against this schema.

## Machine-Readable Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AccountResearchAgentOutput",
  "type": "object",
  "required": [
    "summary",
    "confidence",
    "sources",
    "decision_action",
    "account_brief",
    "relationship_map",
    "opportunity_context",
    "service_context",
    "buying_signals",
    "risks",
    "recommended_research_questions",
    "assumptions",
    "missing_data",
    "source_records"
  ],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Executive one-paragraph account posture"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Overall brief confidence per confidence-scoring.md"
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
    "account_id": { "type": "string" },
    "account_name": { "type": "string" },
    "account_brief": {
      "type": "object",
      "required": ["headline", "snapshot"],
      "properties": {
        "headline": { "type": "string" },
        "snapshot": {
          "type": "object",
          "properties": {
            "tier": { "type": "string" },
            "industry": { "type": "string" },
            "parent_account": { "type": "string" },
            "strategic_value": { "enum": ["tier_1", "tier_2", "tier_3", "unknown"] },
            "total_open_pipeline": { "type": "number" },
            "open_opportunity_count": { "type": "integer" },
            "open_case_count": { "type": "integer" },
            "last_activity_date": { "type": "string", "format": "date" },
            "ninety_day_objectives": {
              "type": "array",
              "items": { "type": "string" }
            }
          }
        },
        "white_space": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "product": { "type": "string" },
              "rationale": { "type": "string" }
            }
          }
        },
        "meeting_prep": {
          "type": "object",
          "description": "Present when user requests meeting prep",
          "properties": {
            "meeting_date": { "type": "string" },
            "attendees": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "contact_id": { "type": "string" },
                  "name": { "type": "string" },
                  "title": { "type": "string" },
                  "role_label": { "type": "string" }
                }
              }
            },
            "recommended_agenda": {
              "type": "array",
              "items": { "type": "string" }
            },
            "recent_activities_summary": { "type": "string" }
          }
        }
      }
    },
    "relationship_map": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["contact_id", "name", "role_label"],
        "properties": {
          "contact_id": { "type": "string" },
          "name": { "type": "string" },
          "title": { "type": "string" },
          "role_label": {
            "enum": [
              "economic_buyer",
              "champion",
              "influencer",
              "blocker",
              "technical_evaluator",
              "end_user",
              "unknown"
            ]
          },
          "role_confidence": {
            "enum": ["confirmed", "inferred", "unknown"]
          },
          "reports_to_contact_id": { "type": "string" },
          "last_engagement_date": { "type": "string", "format": "date" },
          "engagement_summary": { "type": "string" },
          "linked_opportunity_ids": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    },
    "opportunity_context": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["opportunity_id", "name", "stage"],
        "properties": {
          "opportunity_id": { "type": "string" },
          "name": { "type": "string" },
          "stage": { "type": "string" },
          "amount": { "type": "number" },
          "probability": { "type": "number" },
          "close_date": { "type": "string", "format": "date" },
          "owner": { "type": "string" },
          "next_step": { "type": "string" },
          "health": { "enum": ["healthy", "at_risk", "critical", "not_applicable"] }
        }
      }
    },
    "service_context": {
      "type": "object",
      "properties": {
        "open_case_count": { "type": "integer" },
        "p1_p2_open_count": { "type": "integer" },
        "recent_sentiment": {
          "enum": ["positive", "neutral", "frustrated", "unknown"]
        },
        "sla_posture": { "enum": ["green", "yellow", "red", "unknown"] },
        "notable_cases": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "case_id": { "type": "string" },
              "short_description": { "type": "string" },
              "priority": { "type": "string" },
              "state": { "type": "string" }
            }
          }
        },
        "summary": { "type": "string" }
      }
    },
    "buying_signals": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["signal", "strength", "evidence"],
        "properties": {
          "signal": { "type": "string" },
          "strength": { "enum": ["strong", "moderate", "weak"] },
          "evidence": { "type": "string" },
          "source_record_id": { "type": "string" },
          "detected_date": { "type": "string", "format": "date" }
        }
      }
    },
    "risks": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["risk", "severity", "rationale"],
        "properties": {
          "risk": { "type": "string" },
          "severity": { "enum": ["critical", "high", "medium", "low"] },
          "rationale": { "type": "string" },
          "source_record_id": { "type": "string" },
          "mitigation_suggestion": { "type": "string" }
        }
      }
    },
    "recommended_research_questions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["question", "spin_category"],
        "properties": {
          "question": { "type": "string" },
          "spin_category": {
            "enum": ["situation", "problem", "implication", "need_payoff"]
          },
          "targets_gap": { "type": "string" },
          "suggested_contact_role": { "type": "string" }
        }
      }
    },
    "assumptions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["assumption", "basis"],
        "properties": {
          "assumption": { "type": "string" },
          "basis": { "type": "string" }
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
            "enum": ["account", "contact", "opportunity", "case", "activity"]
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
            "enum": ["account", "contact", "opportunity", "case", "activity", "kb", "policy"]
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
        "type": { "enum": ["activity_task", "research_follow_up"] },
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

## Example (Demo — Acme Corporation)

```json
{
  "summary": "Acme Corporation is a Tier-1 strategic account with $420K open pipeline and one at-risk expansion opp. Service posture is yellow due to 2 open P2 cases. Executive meeting prep recommended with CIO and VP Operations.",
  "confidence": 0.88,
  "sources": [
    { "type": "crm", "id": "acct001", "label": "Acme Corporation" },
    { "type": "crm", "id": "opp789", "label": "Acme Expansion FY26" },
    { "type": "policy", "id": "customer_risk_guide", "label": "CUSTOMER_RISK_GUIDE" }
  ],
  "decision_action": "answer",
  "account_id": "acct001",
  "account_name": "Acme Corporation",
  "account_brief": {
    "headline": "Tier-1 account — expansion in flight; resolve P2 cases before QBR",
    "snapshot": {
      "tier": "Tier 1",
      "industry": "Manufacturing",
      "parent_account": null,
      "strategic_value": "tier_1",
      "total_open_pipeline": 420000,
      "open_opportunity_count": 3,
      "open_case_count": 4,
      "last_activity_date": "2026-06-18",
      "ninety_day_objectives": [
        "Close Acme Expansion FY26 ($250K)",
        "Resolve integration P2 cases blocking rollout",
        "Identify economic buyer for platform renewal"
      ]
    },
    "white_space": [
      {
        "product": "Advanced Analytics Module",
        "rationale": "No opp or case references; peer tier-1 accounts in manufacturing commonly adopt"
      }
    ],
    "meeting_prep": {
      "meeting_date": "2026-07-02",
      "attendees": [
        {
          "contact_id": "con101",
          "name": "Sarah Chen",
          "title": "CIO",
          "role_label": "economic_buyer"
        },
        {
          "contact_id": "con102",
          "name": "Marcus Webb",
          "title": "VP Operations",
          "role_label": "champion"
        }
      ],
      "recommended_agenda": [
        "Expansion project status and timeline",
        "Open integration issues and resolution plan",
        "ROI metrics from Phase 1 deployment",
        "Analytics module evaluation scope"
      ],
      "recent_activities_summary": "Demo completed 2026-06-18; no executive touchpoint in 45 days."
    }
  },
  "relationship_map": [
    {
      "contact_id": "con101",
      "name": "Sarah Chen",
      "title": "CIO",
      "role_label": "economic_buyer",
      "role_confidence": "inferred",
      "last_engagement_date": "2026-05-15",
      "engagement_summary": "Attended Q1 business review; not on recent expansion calls",
      "linked_opportunity_ids": ["opp789"]
    },
    {
      "contact_id": "con102",
      "name": "Marcus Webb",
      "title": "VP Operations",
      "role_label": "champion",
      "role_confidence": "confirmed",
      "last_engagement_date": "2026-06-18",
      "engagement_summary": "Primary contact on Expansion opp; drove demo attendance",
      "linked_opportunity_ids": ["opp789", "opp790"]
    }
  ],
  "opportunity_context": [
    {
      "opportunity_id": "opp789",
      "name": "Acme Expansion FY26",
      "stage": "Proposal",
      "amount": 250000,
      "probability": 45,
      "close_date": "2026-07-15",
      "owner": "Jordan Lee",
      "next_step": "Executive alignment with CIO",
      "health": "at_risk"
    }
  ],
  "service_context": {
    "open_case_count": 4,
    "p1_p2_open_count": 2,
    "recent_sentiment": "frustrated",
    "sla_posture": "yellow",
    "notable_cases": [
      {
        "case_id": "cs2001",
        "short_description": "Integration API timeout in production",
        "priority": "2",
        "state": "In Progress"
      }
    ],
    "summary": "Two P2 integration cases open 12+ days; customer notes cite rollout delay impact."
  },
  "buying_signals": [
    {
      "signal": "Expansion opp advanced to Proposal within 30 days",
      "strength": "strong",
      "evidence": "Stage changed Proposal 2026-06-01; amount $250K",
      "source_record_id": "opp789",
      "detected_date": "2026-06-01"
    },
    {
      "signal": "Executive QBR scheduled",
      "strength": "moderate",
      "evidence": "Activity logged: Executive QBR 2026-07-02",
      "source_record_id": "act550",
      "detected_date": "2026-06-20"
    }
  ],
  "risks": [
    {
      "risk": "Open P2 cases correlated with slipping expansion close date",
      "severity": "high",
      "rationale": "Close date moved once; 2 P2 cases open per CUSTOMER_RISK_GUIDE",
      "source_record_id": "cs2001",
      "mitigation_suggestion": "Escalate case resolution before QBR; include status in meeting agenda"
    },
    {
      "risk": "No confirmed economic buyer engagement on late-stage opp",
      "severity": "medium",
      "rationale": "CIO last activity 45+ days ago on $250K Proposal opp",
      "source_record_id": "opp789",
      "mitigation_suggestion": "Secure CIO attendance and alignment on expansion ROI"
    }
  ],
  "recommended_research_questions": [
    {
      "question": "What business outcomes must the expansion deliver by end of Q3?",
      "spin_category": "need_payoff",
      "targets_gap": "economic_buyer priorities undocumented",
      "suggested_contact_role": "economic_buyer"
    },
    {
      "question": "How are the open integration issues affecting your rollout timeline?",
      "spin_category": "implication",
      "targets_gap": "case-to-opp impact unquantified",
      "suggested_contact_role": "champion"
    },
    {
      "question": "Who else needs to sign off before you can move forward with the expansion?",
      "spin_category": "situation",
      "targets_gap": "buying committee incomplete in CRM",
      "suggested_contact_role": "champion"
    }
  ],
  "assumptions": [
    {
      "assumption": "Sarah Chen (CIO) is the economic buyer for Expansion FY26",
      "basis": "Title and QBR attendance pattern; not tagged as economic buyer in CRM"
    }
  ],
  "missing_data": [
    {
      "field": "economic_buyer",
      "object": "opportunity",
      "impact": "Cannot confirm budget authority for expansion close plan"
    }
  ],
  "source_records": [
    { "object": "account", "id": "acct001", "label": "Acme Corporation", "fields_used": ["tier", "industry"] },
    { "object": "opportunity", "id": "opp789", "label": "Acme Expansion FY26", "fields_used": ["stage", "amount", "close_date"] },
    { "object": "case", "id": "cs2001", "label": "Integration API timeout", "fields_used": ["priority", "state"] },
    { "object": "contact", "id": "con102", "label": "Marcus Webb", "fields_used": ["title", "last_activity"] }
  ]
}
```

## Field Notes

- `confidence` reflects overall brief quality per [shared/confidence-scoring.md](../../shared/confidence-scoring.md)
- Empty arrays are valid when no signals/risks exist — do not omit required arrays
- `meeting_prep` nested under `account_brief` when user requests meeting context
- `source_records` is the authoritative audit trail; `sources` remains for runtime compatibility
