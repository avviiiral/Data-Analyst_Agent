from __future__ import annotations

from backend.framework.registry import registry


class AgentPool:

    def __init__(self):

        self._agents = {}

        self.reload()

    def reload(self):

        self._agents.clear()

        for agent in registry.all():

            self._agents[agent.name] = agent

    def get(
        self,
        name: str,
    ):

        return self._agents.get(name)

    def all(self):

        return list(self._agents.values())

    def names(self):

        return sorted(self._agents.keys())

    def count(self):

        return len(self._agents)


agent_pool = AgentPool()