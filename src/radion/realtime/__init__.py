"""Radion realtime (WebSocket) product surface."""

from __future__ import annotations

from .channels import (
    CHANNELS,
    FILTER_REQUIREMENTS,
    Channel,
    FilterKey,
    MempoolChannel,
    SubscribableChannel,
    is_channel,
    is_mempool_channel,
    is_subscribable_channel,
)
from .client import RealtimeClient
from .dispatcher import EventDispatcher
from .payloads import (
    ActivityPayload,
    AnyChannelPayload,
    AnyConfirmedPayload,
    CollateralPayload,
    CombosPayload,
    LifecyclePayload,
    OraclePayload,
    PricesPayload,
    TradesPayload,
)
from .protocol import (
    ChannelEvent,
    ChannelFilters,
    ErrorFrame,
    EventFrame,
    InboundFrame,
    PongFrame,
    SubscribedFrame,
    Subscription,
    UnsubscribedFrame,
    parse_inbound_frame,
    validate_subscription_filters,
)
from .reconnect_manager import ReconnectManager
from .subscription_manager import SubscriptionManager

__all__ = [
    "CHANNELS",
    "FILTER_REQUIREMENTS",
    "ActivityPayload",
    "AnyChannelPayload",
    "AnyConfirmedPayload",
    "Channel",
    "ChannelEvent",
    "ChannelFilters",
    "CollateralPayload",
    "CombosPayload",
    "ErrorFrame",
    "EventDispatcher",
    "EventFrame",
    "FilterKey",
    "InboundFrame",
    "LifecyclePayload",
    "MempoolChannel",
    "OraclePayload",
    "PongFrame",
    "PricesPayload",
    "RealtimeClient",
    "ReconnectManager",
    "SubscribableChannel",
    "SubscribedFrame",
    "Subscription",
    "SubscriptionManager",
    "TradesPayload",
    "UnsubscribedFrame",
    "is_channel",
    "is_mempool_channel",
    "is_subscribable_channel",
    "parse_inbound_frame",
    "validate_subscription_filters",
]
