"""Shared configuration for the Radion SDK."""

from __future__ import annotations

from dataclasses import dataclass

DEFAULT_BASE_URL = "https://api.radion.app"
"""Default base URL for the Radion REST API."""

DEFAULT_WS_URL = "wss://api.radion.app/ws"
"""Default endpoint for the Radion realtime (WebSocket) API."""


@dataclass(frozen=True, slots=True)
class RadionConfig:
    """Shared configuration for every Radion product surface.

    ``base_url`` is reserved for the forthcoming REST resource namespaces
    (``markets``, ``traders``, ``backtests``, …); the realtime client uses
    ``ws_url``.
    """

    api_key: str
    base_url: str = DEFAULT_BASE_URL
    ws_url: str = DEFAULT_WS_URL
