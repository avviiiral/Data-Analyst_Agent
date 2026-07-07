from __future__ import annotations

from typing import Type

from backend.framework.base_agent import BaseAgent


class AgentRegistry:

    def __init__(self) -> None:

        self._agents: dict[str, Type[BaseAgent]] = {}

    def register(
        self,
        agent_class: Type[BaseAgent],
    ) -> None:

        self._agents[agent_class.name] = agent_class

    def unregister(
        self,
        agent_name: str,
    ) -> None:

        self._agents.pop(agent_name, None)

    def exists(
        self,
        agent_name: str,
    ) -> bool:

        return agent_name in self._agents

    def get(
        self,
        agent_name: str,
    ) -> Type[BaseAgent]:

        return self._agents[agent_name]

    def create(
        self,
        agent_name: str,
    ) -> BaseAgent:

        return self.get(agent_name)()

    def names(
        self,
    ) -> list[str]:

        return sorted(self._agents.keys())

    def all(
        self,
    ) -> list[Type[BaseAgent]]:

        return list(self._agents.values())

    def items(
        self,
    ):

        return self._agents.items()

    def count(
        self,
    ) -> int:

        return len(self._agents)

    def clear(
        self,
    ) -> None:

        self._agents.clear()


registry = AgentRegistry()