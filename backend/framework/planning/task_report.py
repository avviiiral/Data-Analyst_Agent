from __future__ import annotations

from backend.framework.planning.execution_plan import ExecutionPlan


class TaskReport:

    def generate(
        self,
        plan: ExecutionPlan,
    ) -> dict:

        completed = 0
        failed = 0
        pending = 0

        details = []

        for task in plan.tasks:

            state_name = task.state.value

            if state_name == "COMPLETED":
                completed += 1

            elif state_name == "FAILED":
                failed += 1

            else:
                pending += 1

        
            details.append(
                {
                    "task": task.name,
                    "agent": task.agent,
                    "priority": task.priority,
                    "state": state_name,
                    "dependencies": list(task.dependencies),
                }
            )

        success_rate = 0.0

        if plan.tasks:

            success_rate = round(
                completed / len(plan.tasks) * 100,
                2,
            )

        return {
            "total_tasks": len(plan.tasks),
            "completed": completed,
            "failed": failed,
            "pending": pending,
            "success_rate": success_rate,
            "details": details,
        }


task_report = TaskReport()