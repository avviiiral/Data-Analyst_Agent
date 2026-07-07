from __future__ import annotations

from typing import Any


class Blackboard:

    def __init__(self):

        self._data: dict[str, Any] = {}

    def write(
        self,
        key: str,
        value: Any,
    ):

        self._data[key] = value

    def read(
        self,
        key: str,
        default=None,
    ):

        return self._data.get(key, default)

    def update(
        self,
        values: dict,
    ):

        self._data.update(values)

    def delete(
        self,
        key: str,
    ):

        self._data.pop(key, None)

    def exists(
        self,
        key: str,
    ):

        return key in self._data

    def keys(self):

        return sorted(self._data.keys())

    def values(self):

        return list(self._data.values())

    def items(self):

        return self._data.items()

    def snapshot(self):

        return dict(self._data)

    def clear(self):

        self._data.clear()


blackboard = Blackboard()