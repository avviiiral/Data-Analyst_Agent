from __future__ import annotations

from collections import deque

from backend.framework.task import Task


class ExecutionDAG:
    """
    Creates dependency-aware execution levels.

    Example:

    Statistics
          │
      ┌───┴────┐
      ▼        ▼
    Correlation Visualization
          │        │
          └───┬────┘
              ▼
           Insights
    """

    def build(
        self,
        tasks: list[Task],
    ) -> list[list[Task]]:

        completed: set[str] = set()

        remaining = tasks[:]

        levels: list[list[Task]] = []

        while remaining:

            ready = []

            waiting = deque()

            for task in remaining:

                if all(
                    dependency in completed
                    for dependency in task.dependencies
                ):
                    ready.append(task)
                else:
                    waiting.append(task)

            if not ready:
                raise RuntimeError(
                    "Circular dependency detected."
                )

            levels.append(ready)

            for task in ready:

                if task.assigned_agent:
                    completed.add(task.assigned_agent)

            remaining = list(waiting)


        return levels


execution_dag = ExecutionDAG()