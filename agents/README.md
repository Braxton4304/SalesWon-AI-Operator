# Agents

Implements: [specifications/agent-spec.md](../specifications/agent-spec.md)

## Creating a New Agent

```powershell
Copy-Item -Recurse agents\_template agents\your-agent-name
```

Edit all files in the new folder. Link to specs in `AGENT.md`.

## Import Contract

```text
Agent Response =
  shared/ (industry IP)
  + runtime/ (orchestration, decision engine, governance)
  + platform/ (CRM via data-spec)
  + agent/ (domain expertise)
  + customer config (Layer 4)
  + CRM context (Layer 5)
```

Agents own domain expertise only. Never redefine runtime or governance.

## Template

Copy from [_template/](_template/) — Reference Agent with inline guidance.
