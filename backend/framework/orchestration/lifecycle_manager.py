from __future__ import annotations

from datetime import datetime


class LifecycleManager:

    def __init__(self):

        self._agents = {}

    def register(
        self,
        agent: str,
    ) -> None:

        self._agents[agent] = {
            "state": "CREATED",
            "created": datetime.now(),
            "started": None,
            "finished": None,
        }

    def start(
        self,
        agent: str,
    ) -> None:

        if agent not in self._agents:
            self.register(agent)

        self._agents[agent]["state"] = "RUNNING"
        self._agents[agent]["started"] = datetime.now()

    def finish(
        self,
        agent: str,
    ) -> None:

        if agent not in self._agents:
            return

        self._agents[agent]["state"] = "COMPLETED"
        self._agents[agent]["finished"] = datetime.now()

    def fail(
        self,
        agent: str,
    ) -> None:

        if agent not in self._agents:
            return

        self._agents[agent]["state"] = "FAILED"
        self._agents[agent]["finished"] = datetime.now()

    def state(
        self,
        agent: str,
    ):

        return self._agents.get(agent)

    def all(self):

        return self._agents


lifecycle_manager = LifecycleManager()