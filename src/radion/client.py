"""The unified :class:`Radion` platform client."""

from __future__ import annotations

from typing import Any

from ._config import DEFAULT_BASE_URL, DEFAULT_WS_URL
from .errors import RadionConnectionError
from .realtime import RealtimeClient
from .rest import AuthenticatedClient


class Radion:
    """Unified async entry point for the Radion platform.

    Holds shared configuration and exposes each product surface as an
    attribute: :attr:`realtime` for the WebSocket stream and :attr:`rest`, an
    authenticated REST client generated from the public OpenAPI schema. Both
    use the shared API key and base URL.

    Extra keyword arguments are forwarded to the realtime client (for example
    ``reconnect``, ``heartbeat``, ``heartbeat_interval``).

    Example::

        radion = Radion(api_key=os.getenv("RADION_API_KEY"))

        # REST
        from radion.rest.api.markets import list_markets

        markets = await list_markets.asyncio(client=radion.rest, limit=10)

        # Realtime
        await radion.realtime.connect()
        await radion.realtime.subscribe("trades")
    """

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        ws_url: str = DEFAULT_WS_URL,
        **realtime_options: Any,
    ) -> None:
        if not api_key:
            raise RadionConnectionError("api_key is required")
        self._base_url = base_url
        self.realtime = RealtimeClient(
            api_key=api_key,
            url=ws_url,
            **realtime_options,
        )
        self.rest = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            prefix="",
            auth_header_name="X-API-Key",
        )
