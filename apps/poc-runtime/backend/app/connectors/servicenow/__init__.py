"""ServiceNow adapter module."""

from app.connectors.servicenow.adapter import ServiceNowAdapter
from app.connectors.servicenow.config import ServiceNowConfig

__all__ = ["ServiceNowAdapter", "ServiceNowConfig"]
