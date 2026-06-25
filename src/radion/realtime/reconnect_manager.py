"""Exponential-backoff timing policy for reconnect attempts."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(slots=True)
class ReconnectManager:
    """Computes exponential-backoff delays for reconnect attempts.

    Owns only the timing policy. The client decides when to reconnect and calls
    :meth:`reset` on graceful shutdown so no further attempts are scheduled.
    """

    initial_delay: float = 0.5
    max_delay: float = 30.0
    factor: float = 2.0
    jitter: float = 0.2
    _attempt: int = 0

    @property
    def attempts(self) -> int:
        """Number of retries since the last successful connection."""
        return self._attempt

    def next_delay(self) -> float:
        """Advance the counter and return the next delay, in seconds."""
        base = min(self.initial_delay * self.factor**self._attempt, self.max_delay)
        self._attempt += 1
        spread = base * self.jitter
        return base - spread / 2 + spread * self._pseudo_jitter()

    def reset(self) -> None:
        """Clear backoff state after a successful connection or shutdown."""
        self._attempt = 0

    def _pseudo_jitter(self) -> float:
        # Cheap, dependency-free spread derived from the attempt count.
        x = math.sin(self._attempt * 12.9898) * 43758.5453
        return x - math.floor(x)
