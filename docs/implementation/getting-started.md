# Getting Started

Create your first SalesWon AI agent in five steps.

## 1. Read the Specs

Start with [specifications/README.md](../../specifications/README.md):

- [agent-spec.md](../../specifications/agent-spec.md) — required files
- [data-spec.md](../../specifications/data-spec.md) — CRM permissions
- [governance-spec.md](../../specifications/governance-spec.md) — confidence and audit

## 2. Copy the Template

```powershell
cd c:\Users\brada\SalesWon-AI-Operator
Copy-Item -Recurse agents\_template agents\customer-service
```

## 3. Fill Domain Files

Replace template placeholders in:

- `IDENTITY.md`, `MISSION.md`, `CAPABILITIES.md`, `LIMITATIONS.md`
- `BEHAVIOR.md`, `DECISION_MODEL.md`, `ESCALATION.md`
- Extend `OUTPUT_SCHEMA.md` with role fields (e.g. `customer_sentiment`)

## 4. Link Shared and Platform

In `AGENT.md`, list imports:

- Relevant [shared/](../../shared/) playbooks
- [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) objects this agent uses

## 5. Record Decisions

If you change permissions or add CRM objects:

1. Update [specifications/data-spec.md](../../specifications/data-spec.md)
2. Update [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md)
3. Add ADR to [architecture/DECISIONS.md](../../architecture/DECISIONS.md)

## Do Not

- Copy runtime files into the agent folder
- Create `SOUL.md`, `MEMORY.md`, or `EVALUATION.md`
- Store customer CRM data in this repo

## Next

- [architecture/ROADMAP.md](../../architecture/ROADMAP.md) — Phase 2 runtime SDK
- [docs/architecture/platform-layers.md](../architecture/platform-layers.md) — full layer model
