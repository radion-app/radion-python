"""Tracks desired subscriptions for replay after reconnect."""

from __future__ import annotations

from .protocol import Subscription


class SubscriptionManager:
    """Records which subscriptions the consumer wants active, keyed by id.

    Transport-agnostic: it stores intent so the client can replay it after a
    reconnect to restore active subscriptions.
    """

    def __init__(self) -> None:
        self._subscriptions: dict[str, Subscription] = {}

    def add(self, subscription: Subscription) -> bool:
        """Record subscribe intent. Returns ``True`` if the id is new."""
        is_new = subscription.id not in self._subscriptions
        self._subscriptions[subscription.id] = subscription
        return is_new

    def remove(self, subscription_id: str) -> bool:
        """Drop intent for ``subscription_id``. Returns ``True`` if present."""
        return self._subscriptions.pop(subscription_id, None) is not None

    def has(self, subscription_id: str) -> bool:
        """Whether a subscription with ``subscription_id`` is desired."""
        return subscription_id in self._subscriptions

    @property
    def desired(self) -> list[Subscription]:
        """Snapshot of every subscription that should be active."""
        return list(self._subscriptions.values())
