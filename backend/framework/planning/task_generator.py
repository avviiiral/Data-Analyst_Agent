from __future__ import annotations

from backend.framework.agent_router import router
from backend.framework.planning.intent_detector import IntentDetector
from backend.framework.planning.intents import Intent
from backend.framework.planning.task import PlanningTask


class TaskGenerator:

    TASK_MAP = {
        Intent.PROFILE: "Profile Dataset",
        Intent.SCHEMA: "Analyze Schema",
        Intent.STATISTICS: "Generate Statistics",
        Intent.CORRELATION: "Analyze Correlation",
        Intent.DISTRIBUTION: "Analyze Distribution",
        Intent.OUTLIER: "Detect Outliers",
        Intent.QUALITY: "Analyze Quality",
        Intent.HEALTH: "Analyze Health",
        Intent.INSIGHT: "Generate Insights",
        Intent.KPI: "Generate KPIs",
        Intent.SUMMARY: "Generate Summary",
        Intent.VISUALIZATION: "Generate Visualization",
        Intent.FORECAST: "Forecast Data",
        Intent.TREND: "Analyze Trend",
        Intent.TIMESERIES: "Analyze Time Series",
        Intent.ANOMALY: "Detect Anomalies",
        Intent.DASHBOARD: "Generate Dashboard",
        Intent.REPORT: "Generate Report",
        Intent.AUTOML: "Run AutoML",
        Intent.REGRESSION: "Run Regression",
        Intent.CLASSIFICATION: "Run Classification",
        Intent.CLUSTERING: "Run Clustering",
    }

    @classmethod
    def generate(
        cls,
        query: str,
    ) -> list[PlanningTask]:

        intents = IntentDetector.detect(query)

        tasks: list[PlanningTask] = []

        added: set[str] = set()

        def add_task(intent: Intent):

            if intent == Intent.UNKNOWN:
                return

            task_name = cls.TASK_MAP[intent]

            if task_name in added:
                return

            tasks.append(
                PlanningTask(
                    name=task_name,
                    agent=router.route(task_name),
                )
            )

            added.add(task_name)

        # ------------------------------------------------------------------
        # Add tasks directly detected from the user query
        # ------------------------------------------------------------------

        for intent in intents:
            add_task(intent)

        # ------------------------------------------------------------------
        # Automatically expand dependency chain
        # ------------------------------------------------------------------

        changed = True

        while changed:

            changed = False

            task_names = {task.name for task in tasks}

            # Statistics requires dataset profiling

            if (
                "Generate Statistics" in task_names
                and "Profile Dataset" not in task_names
            ):
                add_task(Intent.PROFILE)
                changed = True

            # Correlation requires statistics

            task_names = {task.name for task in tasks}

            if (
                "Analyze Correlation" in task_names
                and "Generate Statistics" not in task_names
            ):
                add_task(Intent.STATISTICS)
                changed = True

            # Dashboard requires visualization + statistics

            task_names = {task.name for task in tasks}

            if (
                "Generate Dashboard" in task_names
                and "Generate Visualization" not in task_names
            ):
                add_task(Intent.VISUALIZATION)
                changed = True

            if (
                "Generate Dashboard" in task_names
                and "Generate Statistics" not in task_names
            ):
                add_task(Intent.STATISTICS)
                changed = True

            # Report requires dashboard + summary

            task_names = {task.name for task in tasks}

            if (
                "Generate Report" in task_names
                and "Generate Dashboard" not in task_names
            ):
                add_task(Intent.DASHBOARD)
                changed = True

            if (
                "Generate Report" in task_names
                and "Generate Summary" not in task_names
            ):
                add_task(Intent.SUMMARY)
                changed = True

            # Summary requires insights + statistics

            task_names = {task.name for task in tasks}

            if (
                "Generate Summary" in task_names
                and "Generate Insights" not in task_names
            ):
                add_task(Intent.INSIGHT)
                changed = True

            if (
                "Generate Summary" in task_names
                and "Generate Statistics" not in task_names
            ):
                add_task(Intent.STATISTICS)
                changed = True

            # Insights require statistics + correlation

            task_names = {task.name for task in tasks}

            if (
                "Generate Insights" in task_names
                and "Generate Statistics" not in task_names
            ):
                add_task(Intent.STATISTICS)
                changed = True

            if (
                "Generate Insights" in task_names
                and "Analyze Correlation" not in task_names
            ):
                add_task(Intent.CORRELATION)
                changed = True

            # Forecast requires statistics

            task_names = {task.name for task in tasks}

            if (
                "Forecast Data" in task_names
                and "Generate Statistics" not in task_names
            ):
                add_task(Intent.STATISTICS)
                changed = True

            # ML tasks require statistics

            task_names = {task.name for task in tasks}

            for ml_task in [
                "Run Regression",
                "Run Classification",
                "Run Clustering",
                "Run AutoML",
            ]:

                if (
                    ml_task in task_names
                    and "Generate Statistics" not in task_names
                ):
                    add_task(Intent.STATISTICS)
                    changed = True

        return tasks