"""The unified :class:`Radion` platform client."""

from __future__ import annotations

from typing import Any

from ._config import DEFAULT_BASE_URL, DEFAULT_WS_URL
from .errors import RadionConnectionError
from .realtime import RealtimeClient


class Radion:
    """Unified async entry point for the Radion platform.

    Holds shared configuration and exposes each product surface as an
    attribute. Today that is :attr:`realtime`; REST resource namespaces
    (``markets``, ``traders``, ``backtests``, ``auth``, ``health``) attach here
    as they ship, built from ``base_url`` over a shared HTTP transport — the
    constructor shape stays stable so adding them is purely additive.

    Extra keyword arguments are forwarded to the realtime client (for example
    ``reconnect``, ``heartbeat``, ``heartbeat_interval``).

    Example::

        radion = Radion(api_key=os.getenv("RADION_API_KEY"))
        await radion.realtime.connect()
        await radion.realtime.subscribe("trades")

        @radion.realtime.on("trades")
        async def handle_trade(event):
            print(event.data)
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
