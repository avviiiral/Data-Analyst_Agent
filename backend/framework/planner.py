from __future__ import annotations

from backend.framework.task import Task


class TaskPlanner:
    """
    Converts a user request into executable tasks.
    """

    def plan(self, request: str) -> list[Task]:

        request = request.lower()

        tasks: list[Task] = []

        if any(
            word in request
            for word in [
                "profile",
                "overview",
                "summary",
            ]
        ):
            tasks.append(Task(name="Profile Dataset"))

        if any(
            word in request
            for word in [
                "statistics",
                "stats",
                "describe",
            ]
        ):
            tasks.append(Task(name="Statistics"))

        if any(
            word in request
            for word in [
                "correlation",
                "relationship",
            ]
        ):
            tasks.append(Task(name="Correlation"))

        if any(
            word in request
            for word in [
                "chart",
                "graph",
                "plot",
                "visualize",
            ]
        ):
            tasks.append(Task(name="Visualization"))

        if any(
            word in request
            for word in [
                "insight",
                "analysis",
                "recommendation",
            ]
        ):
            tasks.append(Task(name="Insights"))

        if any(
            word in request
            for word in [
                "forecast",
                "prediction",
            ]
        ):
            tasks.append(Task(name="Forecast"))

        if not tasks:
            tasks.append(Task(name="General Analysis"))

        self._apply_dependencies(tasks)

        return tasks
    
    def _apply_dependencies(
        self,
        tasks: list[Task],
    ) -> None:

        task_map = {
            task.name: task
            for task in tasks
        }

        if "Correlation" in task_map and "Statistics" in task_map:
            task_map["Correlation"].depends_on(
                "StatisticsAgent"
            )

        if "Visualization" in task_map and "Statistics" in task_map:
            task_map["Visualization"].depends_on(
                "StatisticsAgent"
            )

        if "Insights" in task_map:

            if "Statistics" in task_map:
                task_map["Insights"].depends_on(
                    "StatisticsAgent"
                )

            if "Correlation" in task_map:
                task_map["Insights"].depends_on(
                    "CorrelationAgent"
                )

            if "Visualization" in task_map:
                task_map["Insights"].depends_on(
                    "VisualizationAgent"
                )

        if "Forecast" in task_map and "Statistics" in task_map:
            task_map["Forecast"].depends_on(
                "StatisticsAgent"
            )


planner = TaskPlanner()