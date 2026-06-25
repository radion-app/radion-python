"""Typed inbound / outbound frame models."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

TData = TypeVar("TData")


@dataclass(frozen=True, slots=True)
class ChannelFilters:
    """Server-side filters narrowing the events delivered on a channel.

    Some channels require a filter (for example ``wallets`` needs ``wallets``,
    ``large_trades`` needs ``min_usd``); see the channel docs.
    """

    wallets: list[str] | None = None
    market_ids: list[str] | None = None
    token_ids: list[str] | None = None
    min_usd: int | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialise to a dict, dropping unset fields."""
        fields = {
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
    told apart. ``channel`` may carry a ``mempool.`` prefix.
    """

    id: str
    channel: str
    filters: ChannelFilters | None = None


@dataclass(frozen=True, slots=True)
class ChannelEvent(Generic[TData]):
    """A data event delivered on a subscribed channel.

    ``id`` identifies the subscription it belongs to; ``channel`` is the
    resolved channel name. ``data`` is generic so consumers can parameterise
    the payload type (``ChannelEvent[MyPayload]``); it defaults to ``Any``.
    """

    id: str
    channel: str
    data: TData


@dataclass(frozen=True, slots=True)
class ErrorFrame:
    """Server-reported error frame."""

    message: str
    code: str | None = None
    channel: str | None = None
    id: str | None = None


def subscribe_frame(subscription: Subscription) -> str:
    """Serialise a subscribe request."""
    payload: dict[str, Any] = {
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


def parse_inbound_frame(raw: str | bytes) -> dict[str, Any] | None:
    """Parse a raw frame into a dict, or ``None`` if malformed.

    A frame is malformed when it is not valid JSON, is not an object, or has no
    string ``type`` discriminator. Callers drop malformed frames silently.
    """
    try:
        value = json.loads(raw)
    except (ValueError, TypeError):
        return None
    if not isinstance(value, dict):
        return None
    if not isinstance(value.get("type"), str):
        return None
    return value
