from __future__ import annotations

from backend.framework.planning.plan_builder import plan_builder
from backend.framework.planning.plan_validator import validator
from backend.framework.planning.task_prioritizer import prioritizer
from backend.framework.planning.execution_scheduler import scheduler
from backend.framework.planning.plan_executor import plan_executor


class PlanningPipeline:

    def execute(
        self,
        query: str,
        dataset=None,
        memory=None,
    ):

        plan = plan_builder.build(query)

        valid, errors = validator.validate(plan)

        if not valid:

            raise ValueError("\n".join(errors))

        plan.tasks = prioritizer.prioritize(plan.tasks)

        stages = scheduler.schedule(plan.tasks)

        results = plan_executor.execute(
            plan=plan,
            dataset=dataset,
            memory=memory,
        )

        return {
            "plan": plan,
            "stages": stages,
            "results": results,
        }


planning_pipeline = PlanningPipeline()