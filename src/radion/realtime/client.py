"""The :class:`RealtimeClient` async WebSocket client."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, TypeVar, cast, overload

import websockets
from websockets.asyncio.client import ClientConnection

from .._config import DEFAULT_WS_URL
from ..errors import RadionConnectionError, RadionError, RadionServerError
from .dispatcher import (
    CLIENT_EVENTS,
    ChannelHandler,
    ClientHandler,
    EventDispatcher,
)
from .heartbeat import Heartbeat
from .protocol import (
    ChannelEvent,
    ErrorFrame,
    EventFrame,
    Subscription,
    parse_inbound_frame,
    ping_frame,
    subscribe_frame,
    unsubscribe_frame,
    validate_subscription_filters,
)
from .reconnect_manager import ReconnectManager
from .subscription_manager import SubscriptionManager

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable
    from typing import Literal

    from .payloads import (
        ActivityPayload,
        AnyConfirmedPayload,
        CollateralPayload,
        CombosPayload,
        LifecyclePayload,
        OraclePayload,
        PricesPayload,
        TradesPayload,
    )

    _P = TypeVar("_P")
    #: A handler for events on a specific channel, typed to its payload.
    ChannelHandlerFor = Callable[[ChannelEvent[_P]], "Awaitable[None] | None"]


class RealtimeClient:
    """Lightweight async WebSocket client for the Radion realtime API.

    Owns the connection lifecycle, transparently reconnects with exponential
    backoff after unexpected drops, restores subscriptions on reconnect, and
    routes inbound channel frames to registered handlers.

    Usually reached as ``radion.realtime``, but can be constructed standalone.

    Example::

        client = RealtimeClient(api_key=os.getenv("RADION_API_KEY"))
        await client.connect()
        await client.subscribe(Subscription(id="trades", channel="trades"))

        @client.on("trades")
        async def handle_trade(event):
            print(event.id, event.data)
    """

    def __init__(
        self,
        *,
        api_key: str,
        url: str = DEFAULT_WS_URL,
        reconnect: bool = True,
        heartbeat: bool = True,
        heartbeat_interval: float = 15.0,
        heartbeat_timeout: float = 10.0,
    ) -> None:
        if not api_key:
            raise RadionConnectionError("api_key is required")
        self._api_key = api_key
        self._url = url
        self._dispatcher = EventDispatcher()
        self._subscriptions = SubscriptionManager()
        self._reconnect = ReconnectManager() if reconnect else None
        self._heartbeat = (
            Heartbeat(
                send_ping=self._send_ping,
                on_stale=self._handle_stale,
                interval=heartbeat_interval,
                timeout=heartbeat_timeout,
            )
            if heartbeat
            else None
        )
        self._conn: ClientConnection | None = None
        self._reader: asyncio.Task[None] | None = None
        self._closed = False
        self._open_event = asyncio.Event()

    @property
    def connected(self) -> bool:
        """Whether the underlying socket is currently open."""
        return self._conn is not None

    async def connect(self) -> None:
        """Open the connection and start the read loop.

        Resolves once the socket is established. Raises
        :class:`RadionConnectionError` if the first attempt fails.
        """
        self._closed = False
        await self._open_socket(initial=True)

    async def subscribe(self, subscription: Subscription) -> None:
        """Subscribe to a channel. Replayed automatically after reconnect."""
        self._assert_usable()
        filter_error = validate_subscription_filters(subscription)
        if filter_error is not None:
            raise RadionError(filter_error)
        if self._subscriptions.add(subscription) and self.connected:
            await self._send(subscribe_frame(subscription))

    async def unsubscribe(self, subscription_id: str) -> None:
        """Unsubscribe by subscription id."""
        self._assert_usable()
        if self._subscriptions.remove(subscription_id) and self.connected:
            await self._send(unsubscribe_frame(subscription_id))

    @overload
    def on(
        self, event: Literal["trades", "large_trades"]
    ) -> Callable[
        [ChannelHandlerFor[TradesPayload]], ChannelHandlerFor[TradesPayload]
    ]: ...
    @overload
    def on(
        self, event: Literal["oracle"]
    ) -> Callable[
        [ChannelHandlerFor[OraclePayload]], ChannelHandlerFor[OraclePayload]
    ]: ...
    @overload
    def on(
        self, event: Literal["lifecycle"]
    ) -> Callable[
        [ChannelHandlerFor[LifecyclePayload]], ChannelHandlerFor[LifecyclePayload]
    ]: ...
    @overload
    def on(
        self, event: Literal["activity"]
    ) -> Callable[
        [ChannelHandlerFor[ActivityPayload]], ChannelHandlerFor[ActivityPayload]
    ]: ...
    @overload
    def on(
        self, event: Literal["collateral"]
    ) -> Callable[
        [ChannelHandlerFor[CollateralPayload]],
        ChannelHandlerFor[CollateralPayload],
    ]: ...
    @overload
    def on(
        self, event: Literal["combos"]
    ) -> Callable[
        [ChannelHandlerFor[CombosPayload]], ChannelHandlerFor[CombosPayload]
    ]: ...
    @overload
    def on(
        self, event: Literal["prices"]
    ) -> Callable[
        [ChannelHandlerFor[PricesPayload]], ChannelHandlerFor[PricesPayload]
    ]: ...
    @overload
    def on(
        self, event: Literal["global", "wallets", "markets"]
    ) -> Callable[
        [ChannelHandlerFor[AnyConfirmedPayload]],
        ChannelHandlerFor[AnyConfirmedPayload],
    ]: ...
    @overload
    def on(
        self, event: str
    ) -> Callable[[ChannelHandler | ClientHandler], ChannelHandler | ClientHandler]: ...
    def on(
        self, event: str
    ) -> Callable[[ChannelHandler | ClientHandler], ChannelHandler | ClientHandler]:
        """Register a handler for a channel or lifecycle event.

        Usable as a decorator::

            @client.on("trades")
            async def handle(event): ...

        Use ``"event"`` to receive every channel event regardless of channel.
        Lifecycle events: ``open``, ``close``, ``reconnect``, ``error``.
        Channel handlers receive ``event.data`` narrowed to the channel's
        payload type.
        """

        def register(
            handler: ChannelHandler | ClientHandler,
        ) -> ChannelHandler | ClientHandler:
            if event in CLIENT_EVENTS:
                self._dispatcher.on_client(event, cast("ClientHandler", handler))
            elif event == "event":
                self._dispatcher.on_all(cast("ChannelHandler", handler))
            else:
                self._dispatcher.on_channel(event, cast("ChannelHandler", handler))
            return handler

        return register

    def off(
        self, event: str, handler: ChannelHandler | ClientHandler | None = None
    ) -> None:
        """Remove a handler (or all handlers for ``event``)."""
        if event in CLIENT_EVENTS:
            self._dispatcher.off_client(event, cast("ClientHandler", handler))
        elif event == "event":
            self._dispatcher.off_all(cast("ChannelHandler", handler))
        else:
            self._dispatcher.off_channel(event, cast("ChannelHandler", handler))

    async def close(self, code: int = 1000, reason: str = "client shutdown") -> None:
        """Gracefully shut down. Stops reconnect attempts and closes the socket."""
        self._closed = True
        if self._heartbeat is not None:
            self._heartbeat.stop()
        if self._reconnect is not None:
            self._reconnect.reset()
        conn = self._conn
        self._conn = None
        if conn is not None:
            await conn.close(code, reason)
        if self._reader is not None:
            self._reader.cancel()
            self._reader = None

    async def _open_socket(self, *, initial: bool) -> None:
        try:
            self._conn = await websockets.connect(
                self._url,
                additional_headers={"X-API-Key": self._api_key},
            )
        except Exception as exc:  # surface connect failure / trigger reconnect
            if initial or self._reconnect is None:
                raise RadionConnectionError(str(exc)) from exc
            await self._schedule_reconnect()
            return

        self._open_event.set()
        if self._reconnect is not None:
            self._reconnect.reset()
        # Restore every desired subscription after a (re)connect.
        for subscription in self._subscriptions.desired:
            await self._send(subscribe_frame(subscription))
        if self._heartbeat is not None:
            self._heartbeat.start()
        await self._dispatcher.emit("open")
        self._reader = asyncio.create_task(self._read_loop())

    async def _read_loop(self) -> None:
        conn = self._conn
        if conn is None:
            return
        try:
            async for raw in conn:
                if self._heartbeat is not None:
                    self._heartbeat.mark_alive()
                await self._route(raw)
        except (asyncio.CancelledError, websockets.ConnectionClosed):
            pass
        finally:
            await self._handle_disconnect()

    async def _route(self, raw: str | bytes) -> None:
        frame = parse_inbound_frame(raw)
        if frame is None:
            return
        if isinstance(frame, EventFrame):
            await self._dispatcher.dispatch(
                ChannelEvent(id=frame.id, channel=frame.channel, data=frame.data)
            )
        elif isinstance(frame, ErrorFrame):
            await self._dispatcher.emit(
                "error",
                RadionServerError(
                    frame.message,
                    code=frame.code,
                    channel=frame.channel,
                    id=frame.id,
                ),
            )
        # pong / subscribed / unsubscribed are acks; mark_alive already handled.

    async def _handle_disconnect(self) -> None:
        if self._heartbeat is not None:
            self._heartbeat.stop()
        self._conn = None
        self._open_event.clear()
        await self._dispatcher.emit("close", {"code": 1006, "reason": "disconnected"})
        if self._closed or self._reconnect is None:
            return
        await self._schedule_reconnect()

    async def _schedule_reconnect(self) -> None:
        if self._reconnect is None or self._closed:
            return
        delay = self._reconnect.next_delay()
        await self._dispatcher.emit(
            "reconnect", {"attempt": self._reconnect.attempts, "delay": delay}
        )
        await asyncio.sleep(delay)
        if not self._closed:
            await self._open_socket(initial=False)

    async def _handle_stale(self) -> None:
        await self._dispatcher.emit("error", RadionConnectionError("stale connection"))
        conn = self._conn
        if conn is not None:
            await conn.close(1011, "stale connection")

    async def _send_ping(self) -> None:
        if self.connected:
            await self._send(ping_frame())

    async def _send(self, payload: str) -> None:
        conn = self._conn
        if conn is not None:
            await conn.send(payload)

    def _assert_usable(self) -> None:
        if self._closed:
            raise RadionConnectionError("client has been closed")
