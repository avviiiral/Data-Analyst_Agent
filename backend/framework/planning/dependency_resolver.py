from __future__ import annotations

from backend.framework.planning.task import PlanningTask


class DependencyResolver:

    DEPENDENCIES = {
        "Generate Statistics": ["Profile Dataset"],
        "Analyze Correlation": ["Generate Statistics"],
        "Analyze Distribution": ["Generate Statistics"],
        "Detect Outliers": ["Generate Statistics"],
        "Analyze Quality": ["Profile Dataset"],
        "Analyze Health": ["Analyze Quality"],
        "Generate Insights": [
            "Generate Statistics",
            "Analyze Correlation",
        ],
        "Generate KPIs": ["Generate Statistics"],
        "Generate Summary": [
            "Generate Statistics",
            "Generate Insights",
        ],
        "Generate Visualization": [
            "Generate Statistics",
        ],
        "Generate Dashboard": [
            "Generate Statistics",
            "Generate Visualization",
        ],
        "Generate Report": [
            "Generate Summary",
            "Generate Dashboard",
        ],
        "Forecast Data": [
            "Generate Statistics",
        ],
        "Analyze Trend": [
            "Forecast Data",
        ],
        "Analyze Time Series": [
            "Forecast Data",
        ],
        "Detect Anomalies": [
            "Generate Statistics",
        ],
        "Run Regression": [
            "Generate Statistics",
        ],
        "Run Classification": [
            "Generate Statistics",
        ],
        "Run Clustering": [
            "Generate Statistics",
        ],
        "Run AutoML": [
            "Generate Statistics",
        ],
    }

    @classmethod
    def resolve(
        cls,
        tasks: list[PlanningTask],
    ) -> list[PlanningTask]:

        task_lookup = {
            task.name: task
            for task in tasks
        }

        for task in tasks:

            task.dependencies = cls.DEPENDENCIES.get(
                task.name,
                [],
            )

        return tasks