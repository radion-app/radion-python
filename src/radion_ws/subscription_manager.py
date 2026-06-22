"""Tracks desired channel subscriptions for replay after reconnect."""

from __future__ import annotations

from .channels import Channel


class SubscriptionManager:
    """Records which channels the consumer wants to be subscribed to.

    Transport-agnostic: it stores intent so the client can replay it after a
    reconnect to restore active subscriptions.
    """

    def __init__(self) -> None:
        self._channels: set[Channel] = set()

    def add(self, channel: Channel) -> bool:
        """Record subscribe intent. Returns ``True`` if newly added."""
        if channel in self._channels:
            return False
        self._channels.add(channel)
        return True

    def remove(self, channel: Channel) -> bool:
        """Drop subscribe intent. Returns ``True`` if it was present."""
        if channel not in self._channels:
            return False
        self._channels.discard(channel)
        return True

    def has(self, channel: Channel) -> bool:
        """Whether ``channel`` is in the desired set."""
        return channel in self._channels

    @property
    def desired(self) -> list[Channel]:
        """Snapshot of every channel that should be subscribed."""
        return list(self._channels)
