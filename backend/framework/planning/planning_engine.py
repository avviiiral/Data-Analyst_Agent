from __future__ import annotations

from backend.framework.planning.plan_builder import plan_builder
from backend.framework.planning.plan_validator import validator
from backend.framework.planning.task_prioritizer import prioritizer
from backend.framework.orchestration.dependency_scheduler import (
    dependency_scheduler,
)


class PlanningEngine:

    def create_plan(
        self,
        query: str,
    ):

        plan = plan_builder.build(query)

        valid, errors = validator.validate(
            plan,
        )

        if not valid:

            raise ValueError(
                "\n".join(errors)
            )

        plan.tasks = prioritizer.prioritize(
            plan.tasks,
        )

        stages = dependency_scheduler.schedule(
            plan.tasks,
        )

        return plan, stages


planning_engine = PlanningEngine()