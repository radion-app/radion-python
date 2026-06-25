"""Typed channel names for the Radion realtime API."""

from __future__ import annotations

from typing import Literal, get_args

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
"""A channel name the SDK can subscribe to."""

CHANNELS: tuple[Channel, ...] = get_args(Channel)
"""Every supported channel, as a tuple."""


def is_channel(value: str) -> bool:
    """Return whether ``value`` is a known channel name."""
    return value in CHANNELS
