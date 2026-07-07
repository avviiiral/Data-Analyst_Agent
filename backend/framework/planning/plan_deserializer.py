from __future__ import annotations

import json

from backend.framework.planning.execution_plan import ExecutionPlan
from backend.framework.planning.task import PlanningTask
from backend.framework.planning.task_state import TaskState


class PlanDeserializer:

    def from_dict(
        self,
        data: dict,
    ) -> ExecutionPlan:

        plan = ExecutionPlan(
            query=data["query"],
        )

        for item in data["tasks"]:

            task = PlanningTask(
                name=item["name"],
                agent=item["agent"],
                priority=item["priority"],
                dependencies=item["dependencies"],
                completed=item["completed"],
                state=TaskState(item["state"]),
            )

            plan.add_task(task)

        return plan

    def from_json(
        self,
        text: str,
    ) -> ExecutionPlan:

        return self.from_dict(
            json.loads(text)
        )


plan_deserializer = PlanDeserializer()