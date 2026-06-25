"""Typed channel names for the Radion realtime API."""

from __future__ import annotations

from typing import Literal, TypeGuard, get_args

Channel = Literal[
    "global",
    "trades",
    "activity",
    "lifecycle",
    "oracle",
    "collateral",
    "combos",
    "prices",
    "wallets",
    "markets",
    "large_trades",
]
"""A confirmed channel name the SDK can subscribe to."""

CHANNELS: tuple[Channel, ...] = get_args(Channel)
"""Every supported confirmed channel, as a tuple."""

MempoolChannel = Literal[
    "mempool.global",
    "mempool.trades",
    "mempool.activity",
    "mempool.lifecycle",
    "mempool.oracle",
    "mempool.collateral",
    "mempool.combos",
    "mempool.prices",
    "mempool.wallets",
    "mempool.markets",
    "mempool.large_trades",
]
"""A ``mempool.``-prefixed companion channel."""

SubscribableChannel = Channel | MempoolChannel
"""Any channel accepted by :meth:`RealtimeClient.subscribe`."""

FilterKey = Literal["wallets", "market_ids", "token_ids", "min_usd"]
"""A server-side filter key."""

_MEMPOOL_PREFIX = "mempool."

#: Per-channel filter requirements. ``required_any_of`` means at least one of
#: the listed filters must be present. Channels absent from this map accept no
#: required filters. Mempool companions share their confirmed channel's rules.
FILTER_REQUIREMENTS: dict[Channel, tuple[FilterKey, ...]] = {
    "wallets": ("wallets",),
    "markets": ("market_ids", "token_ids"),
}


def is_channel(value: str) -> TypeGuard[Channel]:
    """Return whether ``value`` is a known confirmed channel name."""
    return value in CHANNELS


def is_mempool_channel(value: str) -> bool:
    """Return whether ``value`` is a ``mempool.``-prefixed channel."""
    return value.startswith(_MEMPOOL_PREFIX) and is_channel(
        value[len(_MEMPOOL_PREFIX) :]
    )


def is_subscribable_channel(value: str) -> bool:
    """Return whether ``value`` is any subscribable channel."""
    return is_channel(value) or is_mempool_channel(value)
