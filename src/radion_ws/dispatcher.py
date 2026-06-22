"""Routes inbound frames to channel and lifecycle handlers."""

from __future__ import annotations

import inspect
from collections.abc import Awaitable, Callable
from typing import Any

from .channels import Channel
from .protocol import ChannelEvent

ChannelHandler = Callable[[ChannelEvent], Awaitable[None] | None]
ClientHandler = Callable[[Any], Awaitable[None] | None]

CLIENT_EVENTS = ("open", "close", "reconnect", "error")


class EventDispatcher:
    """Routes channel events to channel handlers and lifecycle events to
    lifecycle handlers.

    Handlers may be sync or async. Per the MVP constraints a throwing consumer
    handler is reported through the ``error`` lifecycle event and never retried,
    and never blocks delivery to other handlers.
    """

    def __init__(self) -> None:
        self._channel_handlers: dict[Channel, list[ChannelHandler]] = {}
        self._client_handlers: dict[str, list[ClientHandler]] = {}

    def on_channel(self, channel: Channel, handler: ChannelHandler) -> None:
        self._channel_handlers.setdefault(channel, []).append(handler)

    def off_channel(
        self, channel: Channel, handler: ChannelHandler | None = None
    ) -> None:
        if handler is None:
            self._channel_handlers.pop(channel, None)
            return
        handlers = self._channel_handlers.get(channel)
        if handlers and handler in handlers:
            handlers.remove(handler)

    def on_client(self, event: str, handler: ClientHandler) -> None:
        self._client_handlers.setdefault(event, []).append(handler)

    def off_client(self, event: str, handler: ClientHandler | None = None) -> None:
        if handler is None:
            self._client_handlers.pop(event, None)
            return
        handlers = self._client_handlers.get(event)
        if handlers and handler in handlers:
            handlers.remove(handler)

    async def dispatch(self, event: ChannelEvent) -> None:
        """Deliver a channel event to every handler for its channel."""
        for handler in list(self._channel_handlers.get(event.channel, [])):
            await self._safely(handler, event)

    async def emit(self, event: str, payload: Any = None) -> None:
        """Emit a lifecycle event to its handlers."""
        for handler in list(self._client_handlers.get(event, [])):
            if event == "error":
                # error handlers must not recurse into the error path.
                await _call(handler, payload)
            else:
                await self._safely(handler, payload)

    async def _safely(self, handler: Callable[..., Any], payload: Any) -> None:
        try:
            await _call(handler, payload)
        except Exception as exc:  # isolate consumer failures, never retry
            await self.emit("error", exc)


async def _call(handler: Callable[..., Any], payload: Any) -> None:
    result = handler(payload)
    if inspect.isawaitable(result):
        await result
