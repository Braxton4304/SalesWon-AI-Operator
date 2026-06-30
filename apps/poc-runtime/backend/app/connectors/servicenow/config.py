# implements: platform/servicenow.md

"""ServiceNow adapter configuration from environment variables."""

from __future__ import annotations

from dataclasses import dataclass

from app.config.settings import Settings, get_settings


@dataclass
class ServiceNowConfig:
    instance_url: str
    client_id: str
    client_secret: str
    username: str
    password_or_token: str

    @classmethod
    def from_settings(cls, settings: Settings | None = None) -> "ServiceNowConfig":
        settings = settings or get_settings()
        return cls(
            instance_url=settings.servicenow_instance_url,
            client_id=settings.servicenow_client_id,
            client_secret=settings.servicenow_client_secret,
            username=settings.servicenow_username,
            password_or_token=settings.servicenow_password_or_token,
        )

    @property
    def is_configured(self) -> bool:
        return bool(
            self.instance_url
            and self.client_id
            and self.client_secret
            and (self.username or self.password_or_token)
        )
