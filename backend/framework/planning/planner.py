from __future__ import annotations

from backend.framework.planning.task_generator import TaskGenerator
from backend.framework.planning.dependency_resolver import (
    DependencyResolver,
)
from backend.framework.planning.task import PlanningTask


class IntelligentPlanner:

    def plan(
        self,
        query: str,
    ) -> list[PlanningTask]:

        tasks = TaskGenerator.generate(query)

        tasks = DependencyResolver.resolve(tasks)

        return self._sort(tasks)

    def _sort(
        self,
        tasks: list[PlanningTask],
    ) -> list[PlanningTask]:

        lookup = {
            task.name: task
            for task in tasks
        }

        ordered = []

        visited = set()

        def visit(name: str):

            if name in visited:
                return

            task = lookup.get(name)

            if task is None:
                return

            for dependency in task.dependencies:

                visit(dependency)

            visited.add(name)

            ordered.append(task)

        for task in tasks:

            visit(task.name)

        return ordered


planner = IntelligentPlanner()