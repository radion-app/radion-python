"""Error types raised by the SDK."""

from __future__ import annotations


class RadionError(Exception):
    """Base class for every error surfaced by the SDK."""


class RadionConnectionError(RadionError):
    """Raised when the SDK is used against an invalid connection state."""


class RadionServerError(RadionError):
    """Raised when the server reports an ``error`` frame."""

    def __init__(
        self,
        message: str,
        *,
        code: str | None = None,
        channel: str | None = None,
        id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.channel = channel
        self.id = id
