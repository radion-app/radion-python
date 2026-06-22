"""Async WebSocket SDK for the Radion realtime API."""

from __future__ import annotations

from .channels import CHANNELS, Channel, is_channel
from .client import RadionWS
from .dispatcher import EventDispatcher
from .errors import RadionConnectionError, RadionError, RadionServerError
from .protocol import ChannelEvent, ErrorFrame
from .reconnect_manager import ReconnectManager
from .subscription_manager import SubscriptionManager

__all__ = [
    "CHANNELS",
    "Channel",
    "ChannelEvent",
    "ErrorFrame",
    "EventDispatcher",
    "RadionConnectionError",
    "RadionError",
    "RadionServerError",
    "RadionWS",
    "ReconnectManager",
    "SubscriptionManager",
    "is_channel",
]

__version__ = "0.1.0"
