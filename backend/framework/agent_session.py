from __future__ import annotations

from datetime import datetime
from uuid import uuid4
from typing import Any

from backend.framework.planning.task import PlanningTask


class AgentSession:

    def __init__(self):

        self.id = str(uuid4())

        self.created_at = datetime.utcnow()

        self.dataset: Any = None

        self.user_query: str = ""

        self.plan: list[PlanningTask] = []

        self.results: dict[str, Any] = {}

        self.metadata: dict[str, Any] = {}

    def set_dataset(
        self,
        dataset,
    ):

        self.dataset = dataset

    def set_query(
        self,
        query: str,
    ):

        self.user_query = query

    def add_task(
        self,
        task: PlanningTask,
    ):

        self.plan.append(task)

    def add_result(
        self,
        agent: str,
        result,
    ):

        self.results[agent] = result

    def get_result(
        self,
        agent: str,
    ):

        return self.results.get(agent)

    def set_metadata(
        self,
        key,
        value,
    ):

        self.metadata[key] = value

    def get_metadata(
        self,
        key,
        default=None,
    ):

        return self.metadata.get(key, default)

    def summary(self):

        return {
            "session_id": self.id,
            "query": self.user_query,
            "tasks": len(self.plan),
            "results": len(self.results),
            "created_at": self.created_at,
        }