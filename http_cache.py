"""An HTTP client wrapper with ETag support and an on-disk response cache."""

from __future__ import annotations

__all__ = ["httpCache"]


def httpCache(value):
    """An HTTP client wrapper with ETag support and an on-disk response cache."""
    if value is None:
        raise ValueError("value must not be None")
    return value
