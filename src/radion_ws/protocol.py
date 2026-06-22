"""Typed inbound / outbound frame models."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from .channels import Channel


@dataclass(frozen=True, slots=True)
class ChannelEvent:
    """A data event delivered on a subscribed channel.

    ``event`` is an optional server-defined sub-type. ``data`` stays untyped so
    the MVP remains payload-agnostic; consumers narrow it as needed.
    """

    channel: Channel
    data: Any
    event: str | None = None


@dataclass(frozen=True, slots=True)
class ErrorFrame:
    """Server-reported error frame."""

    message: str
    code: str | None = None
    channel: str | None = None


def subscribe_frame(channel: Channel) -> str:
    """Serialise a subscribe request."""
    return json.dumps({"type": "subscribe", "channel": channel})


def unsubscribe_frame(channel: Channel) -> str:
    """Serialise an unsubscribe request."""
    return json.dumps({"type": "unsubscribe", "channel": channel})


def ping_frame(ts: float) -> str:
    """Serialise a heartbeat ping."""
    return json.dumps({"type": "ping", "ts": ts})


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
