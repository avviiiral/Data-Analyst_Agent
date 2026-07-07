from __future__ import annotations

import json

from backend.framework.planning.execution_plan import ExecutionPlan


class PlanSerializer:

    def to_dict(
        self,
        plan: ExecutionPlan,
    ) -> dict:

        return {
            "query": plan.query,
            "tasks": [
                {
                    "name": task.name,
                    "agent": task.agent,
                    "priority": task.priority,
                    "dependencies": task.dependencies,
                    "completed": task.completed,
                    "state": task.state.value,
                }
                for task in plan.tasks
            ],
        }

    def to_json(
        self,
        plan: ExecutionPlan,
        indent: int = 4,
    ) -> str:

        return json.dumps(
            self.to_dict(plan),
            indent=indent,
        )


plan_serializer = PlanSerializer()