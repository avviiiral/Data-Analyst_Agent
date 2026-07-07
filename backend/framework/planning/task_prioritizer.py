from __future__ import annotations

from backend.framework.planning.task import PlanningTask


class TaskPrioritizer:

    PRIORITY = {
        "Profile Dataset": 1,
        "Analyze Schema": 1,

        "Generate Statistics": 2,
        "Analyze Quality": 2,
        "Analyze Health": 2,

        "Analyze Correlation": 3,
        "Analyze Distribution": 3,
        "Detect Outliers": 3,
        "Generate KPIs": 3,

        "Generate Insights": 4,
        "Forecast Data": 4,
        "Analyze Trend": 4,
        "Analyze Time Series": 4,
        "Detect Anomalies": 4,

        "Generate Summary": 5,
        "Generate Visualization": 5,

        "Generate Dashboard": 6,

        "Generate Report": 7,

        "Run Regression": 8,
        "Run Classification": 8,
        "Run Clustering": 8,
        "Run AutoML": 8,
    }

    @classmethod
    def prioritize(
        cls,
        tasks: list[PlanningTask],
    ) -> list[PlanningTask]:

        for task in tasks:

            task.priority = cls.PRIORITY.get(
                task.name,
                99,
            )

        return sorted(
            tasks,
            key=lambda task: task.priority,
        )


prioritizer = TaskPrioritizer()