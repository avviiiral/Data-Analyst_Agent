from __future__ import annotations

from backend.framework.agent_executor import executor
from backend.framework.planning.execution_plan import ExecutionPlan


class PlanExecutor:

    def execute(
        self,
        plan: ExecutionPlan,
        dataset=None,
        memory=None,
    ):

        results = []

        for task in plan.tasks:

            if task.agent is None:
                raise ValueError(f"No agent assigned for task '{task.name}'.")

            response = executor.execute(
                agent_name=task.agent,
                dataset=dataset,
                memory=memory,
            )

            task.completed = response.success

            results.append(
                {
                    "task": task.name,
                    "agent": task.agent,
                    "response": response,
                }
            )

        return results


plan_executor = PlanExecutor()