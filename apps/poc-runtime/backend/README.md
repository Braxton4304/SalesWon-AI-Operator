# Backend — SalesWon POC Runtime

FastAPI application. See [docs/poc-runtime/README.md](../../../docs/poc-runtime/README.md).

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
copy .env.example .env
uvicorn app.main:app --reload --port 8001
pytest -v
```
