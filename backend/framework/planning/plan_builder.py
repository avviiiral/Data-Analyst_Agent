from __future__ import annotations

from backend.framework.planning.execution_plan import ExecutionPlan
from backend.framework.planning.planner import planner


class PlanBuilder:

    def build(
        self,
        query: str,
    ) -> ExecutionPlan:

        tasks = planner.plan(query)

        plan = ExecutionPlan(
            query=query,
        )

        for task in tasks:

            plan.add_task(task)

        return plan


plan_builder = PlanBuilder()