# SalesWon AI POC Runtime v1

Connector-ready local POC shell implementing [runtime-spec](../../specifications/runtime-spec.md), [governance-spec](../../specifications/governance-spec.md), and [data-spec](../../specifications/data-spec.md).

See [docs/poc-runtime/README.md](../../docs/poc-runtime/README.md) for full setup and run instructions.

## Quick Start

### Backend

```bash
cd apps/poc-runtime/backend
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -e ".[dev]"
copy .env.example .env
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd apps/poc-runtime/frontend
npm install
npm run dev
```

Open http://localhost:5173 — set a dev user ID in the sidebar (sent as `X-User-Id` header).

## Architecture

```text
/apps/poc-runtime/
  backend/     FastAPI — POST /chat, POST /chat/confirm, GET /health
  frontend/    React + Vite chat UI
```

No fake demo data. Connector and LLM adapters activate when credentials are supplied via `.env`.
