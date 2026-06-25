"""Typed inbound / outbound frame models."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Generic, TypeVar

import msgspec

from .channels import (
    FILTER_REQUIREMENTS,
    SubscribableChannel,
    is_channel,
    is_mempool_channel,
)
from .payloads import AnyChannelPayload

TData = TypeVar("TData")

_MEMPOOL_PREFIX = "mempool."


@dataclass(frozen=True, slots=True)
class ChannelFilters:
    """Server-side filters narrowing the events delivered on a channel.

    Some channels require a filter (for example ``wallets`` needs ``wallets``,
    ``markets`` needs ``market_ids`` or ``token_ids``); see the channel docs.
    """

    wallets: list[str] | None = None
    market_ids: list[str] | None = None
    token_ids: list[str] | None = None
    min_usd: int | None = None

    def to_dict(self) -> dict[str, object]:
        """Serialise to a dict, dropping unset fields."""
        fields: dict[str, object | None] = {
            "wallets": self.wallets,
            "market_ids": self.market_ids,
            "token_ids": self.token_ids,
            "min_usd": self.min_usd,
        }
        return {key: value for key, value in fields.items() if value is not None}


@dataclass(frozen=True, slots=True)
class Subscription:
    """A single channel subscription.

    ``id`` is a client-defined string echoed back on acknowledgements and on
    every event frame, so multiple subscriptions to the same channel can be
    told apart. ``channel`` is a confirmed channel or its ``mempool.`` companion.
    """

    id: str
    channel: SubscribableChannel
    filters: ChannelFilters | None = None


@dataclass(frozen=True, slots=True)
class ChannelEvent(Generic[TData]):
    """A data event delivered on a subscribed channel.

    ``id`` identifies the subscription it belongs to; ``channel`` is the
    resolved channel name. ``data`` is the channel's typed payload -- handlers
    registered with :meth:`RealtimeClient.on` for a specific channel receive it
    narrowed to that channel's payload type.
    """

    id: str
    channel: str
    data: TData


# --- inbound frame envelopes (validated with msgspec) ----------------------


class EventFrame(msgspec.Struct, tag="event", tag_field="type", frozen=True):
    """A channel data event frame."""

    id: str
    channel: str
    data: dict[str, object]


class SubscribedFrame(msgspec.Struct, tag="subscribed", tag_field="type", frozen=True):
    """Acknowledgement of a subscribe request."""

    id: str
    channel: str | None = None


class UnsubscribedFrame(
    msgspec.Struct, tag="unsubscribed", tag_field="type", frozen=True
):
    """Acknowledgement of an unsubscribe request."""

    id: str
    channel: str | None = None


class PongFrame(msgspec.Struct, tag="pong", tag_field="type", frozen=True):
    """Heartbeat reply to a client ``ping``."""


class ErrorFrame(msgspec.Struct, tag="error", tag_field="type", frozen=True):
    """Server-reported error frame."""

    message: str
    code: str | None = None
    channel: str | None = None
    id: str | None = None
    skipped: int | None = None  # number of dropped events on a ``lagged`` error.


InboundFrame = EventFrame | SubscribedFrame | UnsubscribedFrame | PongFrame | ErrorFrame
"""Any frame the client may receive from the server."""

_FRAME_DECODER = msgspec.json.Decoder(InboundFrame)


def subscribe_frame(subscription: Subscription) -> str:
    """Serialise a subscribe request."""
    payload: dict[str, object] = {
        "action": "subscribe",
        "id": subscription.id,
        "channel": subscription.channel,
    }
    if subscription.filters is not None:
        payload["filters"] = subscription.filters.to_dict()
    return json.dumps(payload)


def unsubscribe_frame(subscription_id: str) -> str:
    """Serialise an unsubscribe request."""
    return json.dumps({"action": "unsubscribe", "id": subscription_id})


def ping_frame() -> str:
    """Serialise a heartbeat ping."""
    return json.dumps({"action": "ping"})


def parse_inbound_frame(raw: str | bytes) -> InboundFrame | None:
    """Parse and validate a raw frame, or return ``None`` if malformed.

    A frame is malformed when it is not valid JSON or does not match a known
    frame envelope. Callers drop malformed frames silently.
    """
    data = raw.encode() if isinstance(raw, str) else raw
    try:
        return _FRAME_DECODER.decode(data)
    except msgspec.MsgspecError:
        return None


def validate_subscription_filters(subscription: Subscription) -> str | None:
    """Validate that a subscription carries the filters its channel requires.

    Returns an error message describing the first violation, or ``None`` when
    the filters satisfy the channel's requirements. Mempool companions share
    their confirmed channel's requirements.
    """
    channel = subscription.channel
    confirmed = (
        channel[len(_MEMPOOL_PREFIX) :] if is_mempool_channel(channel) else channel
    )
    if not is_channel(confirmed):
        return f'unknown channel "{channel}"'
    required_any_of = FILTER_REQUIREMENTS.get(confirmed)
    if required_any_of is None:
        return None
    filters = subscription.filters
    if filters is None or not any(
        _filter_present(filters, key) for key in required_any_of
    ):
        joined = " or ".join(required_any_of)
        return f'channel "{channel}" requires a {joined} filter'
    return None


def _filter_present(filters: ChannelFilters, key: str) -> bool:
    value = getattr(filters, key, None)
    if isinstance(value, list):
        return len(value) > 0
    return value is not None


__all__ = [
    "AnyChannelPayload",
    "ChannelEvent",
    "ChannelFilters",
    "ErrorFrame",
    "EventFrame",
    "InboundFrame",
    "PongFrame",
    "SubscribedFrame",
    "Subscription",
    "UnsubscribedFrame",
    "parse_inbound_frame",
    "ping_frame",
    "subscribe_frame",
    "unsubscribe_frame",
    "validate_subscription_filters",
]
