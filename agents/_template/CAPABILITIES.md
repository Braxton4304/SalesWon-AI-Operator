# Capabilities

What this agent **is allowed** to do. Must align with [data-spec](../../specifications/data-spec.md) permissions.

## Allowed Actions

- Read CRM objects permitted for this role *(list tables)*
- Draft-only writes per data-spec `draft_only` objects
- Answer user questions grounded in CRM + shared playbooks
- Recommend next activities per ACTIVITY_PRIORITIZATION
- Retrieve additional CRM/KB context via runtime decision engine

## Tools

See [TOOLS.md](TOOLS.md). Tool list must match runtime allowlist when SDK is implemented.

## Shared Knowledge

Import from [shared/](../../shared/) as relevant:

- *(e.g. SALES_PLAYBOOK.md chapters 1–3)*
