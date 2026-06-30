"""API module."""

from app.api.chat import router as chat_router
from app.api.confirm import router as confirm_router
from app.api.health import router as health_router

__all__ = ["chat_router", "confirm_router", "health_router"]
