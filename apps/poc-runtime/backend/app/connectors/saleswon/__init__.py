"""SalesWon connector module."""

from app.connectors.saleswon.base import (
    ConnectorNotConfigured,
    Record,
    RecordNotFound,
    SalesWonConnector,
    WriteResult,
)
from app.connectors.saleswon.servicenow import ServiceNowSalesWonConnector

__all__ = [
    "ConnectorNotConfigured",
    "Record",
    "RecordNotFound",
    "SalesWonConnector",
    "ServiceNowSalesWonConnector",
    "WriteResult",
]
