from __future__ import annotations

from typing import Any


class AgentMemory:

    def __init__(self):

        self._global_memory: dict[str, Any] = {}

        self._agent_memory: dict[str, dict[str, Any]] = {}

    def set(self, key: str, value: Any):

        self._global_memory[key] = value

    def get(self, key: str, default=None):

        return self._global_memory.get(key, default)

    def set_agent(self, agent: str, key: str, value: Any):

        if agent not in self._agent_memory:
            self._agent_memory[agent] = {}

        self._agent_memory[agent][key] = value

    def get_agent(self, agent: str, key: str, default=None):

        return self._agent_memory.get(agent, {}).get(key, default)

    def global_keys(self):

        return list(self._global_memory.keys())

    def agent_keys(self, agent: str):

        return list(self._agent_memory.get(agent, {}).keys())

    def clear(self):

        self._global_memory.clear()

        self._agent_memory.clear()


memory = AgentMemory()