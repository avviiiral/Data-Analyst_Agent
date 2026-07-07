from __future__ import annotations

from collections import Counter

from backend.framework.planning.execution_plan import ExecutionPlan
from backend.framework.planning.task_state import TaskState


class TaskMonitor:

    def summary(
        self,
        plan: ExecutionPlan,
    ):

        counter = Counter()

        for task in plan.tasks:

            state = task.state

            if isinstance(state, TaskState):
                counter[state.value] += 1
            else:
                counter[str(state)] += 1

        return dict(counter)

    def progress(
        self,
        plan: ExecutionPlan,
    ) -> float:

        if not plan.tasks:
            return 0.0

        completed = sum(task.completed for task in plan.tasks)

        return round(completed / len(plan.tasks) * 100, 2)


monitor = TaskMonitor()