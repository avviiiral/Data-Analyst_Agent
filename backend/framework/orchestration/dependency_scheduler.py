from __future__ import annotations

from backend.framework.planning.task import PlanningTask


class DependencyScheduler:

    def schedule(
        self,
        tasks: list[PlanningTask],
    ) -> list[list[PlanningTask]]:

        completed: set[str] = set()

        remaining = tasks.copy()

        stages: list[list[PlanningTask]] = []

        while remaining:

            ready = []

            for task in remaining:

                if all(
                    dependency in completed
                    for dependency in task.dependencies
                ):
                    ready.append(task)

            if not ready:

                raise RuntimeError(
                    "Circular dependency detected."
                )

            stages.append(ready)

            for task in ready:

                completed.add(task.name)

                remaining.remove(task)

        return stages


dependency_scheduler = DependencyScheduler()