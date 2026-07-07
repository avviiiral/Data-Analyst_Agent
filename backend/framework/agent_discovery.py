from __future__ import annotations

from backend.framework.registry import registry


class AgentDiscovery:

    @staticmethod
    def all():

        return registry.names()

    @staticmethod
    def exists(
        agent: str,
    ):

        return agent in registry.names()

    @staticmethod
    def search(
        keyword: str,
    ):

        keyword = keyword.lower()

        return [
            agent
            for agent in registry.names()
            if keyword in agent.lower()
        ]

    @staticmethod
    def count():

        return len(registry.names())