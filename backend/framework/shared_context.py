from __future__ import annotations

from typing import Any


class SharedContext:

    def __init__(self):

        self._context: dict[str, Any] = {}

    def set(self, key: str, value: Any):

        self._context[key] = value

    def get(self, key: str, default=None):

        return self._context.get(key, default)

    def update(self, values: dict):

        self._context.update(values)

    def remove(self, key: str):

        self._context.pop(key, None)

    def contains(self, key: str):

        return key in self._context

    def keys(self):

        return sorted(self._context.keys())

    def clear(self):

        self._context.clear()

    def as_dict(self):

        return dict(self._context)


shared_context = SharedContext()