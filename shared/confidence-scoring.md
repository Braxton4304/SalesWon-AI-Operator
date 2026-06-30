# Confidence Scoring

Implements: [specifications/governance-spec.md](../specifications/governance-spec.md)

## Bands

| Band | Range | Behavior |
|------|-------|----------|
| High | ≥ 0.85 | Answer or recommend |
| Medium | 0.60–0.84 | Answer with caveats; human review for writes |
| Low | < 0.60 | Ask, retrieve, or escalate |

## Factors

| Factor | Impact |
|--------|--------|
| CRM required fields present | +confidence |
| Data freshness within window | +confidence |
| RAG + CRM agreement | +confidence |
| Missing required fields | -confidence → missing_data_behavior |
| Stale records | -confidence |
| Conflicting sources | -confidence → escalate |

## CRM Integration

Per-object confidence defaults in [data-spec](../specifications/data-spec.md). Field-level confidence when `confidence: field_dependent`.

## Runtime

Enforced by [runtime/GOVERNANCE.md](../runtime/GOVERNANCE.md) and [runtime/CONFIG.yaml](../runtime/CONFIG.yaml) (see [CONFIG.md](../runtime/CONFIG.md) for annotated copy).
