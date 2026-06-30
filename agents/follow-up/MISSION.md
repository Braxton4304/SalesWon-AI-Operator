# Mission

**Primary outcome:** Reduce revenue leakage from missed follow-ups by surfacing overdue activities, recommending optimal cadence, and producing ready-to-send draft messages — so reps act on the highest-value touchpoints first.

## Success Criteria

| Metric | Target (Phase 1 pilot) |
|--------|------------------------|
| Overdue detection accuracy | ≥ 98% match to ServiceNow due_date/state |
| Follow-up priority acceptance | ≥ 70% |
| Email draft acceptance (send or minor edit) | ≥ 65% |
| Cadence recommendation usefulness | ≥ 75% per rep survey |
| False-positive overdue flags | ≤ 5% |

## Business Reasoning Alignment

Per [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md):

- **Sales Velocity** — Primary. Recover stale deals and close activity gaps quickly.
- **Activity Effectiveness** — Primary. Right message, right time, right record.
- **Revenue** — Secondary. Weight follow-ups by linked opportunity amount × probability.
- **Customer Retention** — Tertiary. Flag executive touchpoints and renewal-adjacent silence.

## ServiceNow Context

Activities on `task`/`activity` (mapped as **activity**), linked **opportunity**, **account**, and **contact** for recipient and context. Overdue = `due_date` past today and state not Closed/Complete; stale opportunity = open opp with no completed activity within cadence window (Layer 4 configurable, default 14 days).
