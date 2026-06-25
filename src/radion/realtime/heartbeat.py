"""Heartbeat loop and stale-connection detection."""

from __future__ import annotations

import asyncio
import time
from collections.abc import Awaitable, Callable


class Heartbeat:
    """Drives the heartbeat loop in a background task.

    Sends a ping every ``interval`` seconds. Any inbound frame counts as
    liveness via :meth:`mark_alive`; if no traffic arrives within ``timeout``
    seconds of the last ping the connection is declared stale and ``on_stale``
    is invoked so the client can reconnect.
    """

    def __init__(
        self,
        *,
        send_ping: Callable[[], Awaitable[None]],
        on_stale: Callable[[], Awaitable[None]],
        interval: float = 15.0,
        timeout: float = 10.0,
    ) -> None:
        self._send_ping = send_ping
        self._on_stale = on_stale
        self._interval = interval
        self._timeout = timeout
        self._task: asyncio.Task[None] | None = None
        self._last_alive = 0.0

    def start(self) -> None:
        """Begin the heartbeat loop. Idempotent."""
        self.stop()
        self._last_alive = time.monotonic()
        self._task = asyncio.create_task(self._run())

    def mark_alive(self) -> None:
        """Record that inbound traffic was seen."""
        self._last_alive = time.monotonic()

    def stop(self) -> None:
        """Stop the heartbeat loop."""
        if self._task is not None:
            self._task.cancel()
            self._task = None

    async def _run(self) -> None:
        try:
            while True:
                await asyncio.sleep(self._interval)
                await self._send_ping()
                if time.monotonic() - self._last_alive > self._interval + self._timeout:
                    await self._on_stale()
                    return
        except asyncio.CancelledError:
            pass
