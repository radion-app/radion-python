"""Radion realtime (WebSocket) product surface."""

from __future__ import annotations

from .channels import CHANNELS, Channel, is_channel
from .client import RealtimeClient
from .dispatcher import EventDispatcher
from .protocol import ChannelEvent, ChannelFilters, ErrorFrame, Subscription
from .reconnect_manager import ReconnectManager
from .subscription_manager import SubscriptionManager

__all__ = [
    "CHANNELS",
    "Channel",
    "ChannelEvent",
    "ChannelFilters",
    "ErrorFrame",
    "EventDispatcher",
    "RealtimeClient",
    "ReconnectManager",
    "Subscription",
    "SubscriptionManager",
    "is_channel",
]
