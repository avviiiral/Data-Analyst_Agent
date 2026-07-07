from __future__ import annotations

from collections import defaultdict

from backend.framework.planning.task import PlanningTask


class ExecutionScheduler:

    @staticmethod
    def schedule(
        tasks: list[PlanningTask],
    ) -> list[list[PlanningTask]]:

        levels = defaultdict(list)

        for task in tasks:

            levels[task.priority].append(task)

        return [
            levels[level]
            for level in sorted(levels)
        ]


scheduler = ExecutionScheduler()