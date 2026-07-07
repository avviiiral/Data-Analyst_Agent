from __future__ import annotations

from backend.framework.planning.execution_plan import ExecutionPlan


class PlanValidator:

    @staticmethod
    def validate(
        plan: ExecutionPlan,
    ) -> tuple[bool, list[str]]:

        errors = []

        task_names = {
            task.name
            for task in plan.tasks
        }

        for task in plan.tasks:

            if task.agent is None:

                errors.append(
                    f"{task.name} has no assigned agent."
                )

            for dependency in task.dependencies:

                if dependency not in task_names:

                    errors.append(
                        f"{task.name} depends on missing task '{dependency}'."
                    )

        return len(errors) == 0, errors


validator = PlanValidator()