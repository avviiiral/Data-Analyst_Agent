from __future__ import annotations

from backend.framework.capability import Capability


class CapabilityRegistry:

    def __init__(self):

        self._capabilities: dict[str, Capability] = {}

    def register(
        self,
        capability: Capability,
    ):

        self._capabilities[capability.name] = capability

    def get(
        self,
        name: str,
    ):

        return self._capabilities.get(name)

    def exists(
        self,
        name: str,
    ):

        return name in self._capabilities

    def names(self):

        return sorted(self._capabilities.keys())

    def count(self):

        return len(self._capabilities)

    def clear(self):

        self._capabilities.clear()


capability_registry = CapabilityRegistry()