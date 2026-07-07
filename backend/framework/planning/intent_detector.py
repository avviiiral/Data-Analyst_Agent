from __future__ import annotations

from backend.framework.planning.intents import Intent


class IntentDetector:

    KEYWORDS = {
        Intent.PROFILE: [
            "profile",
            "overview",
            "dataset",
        ],
        Intent.SCHEMA: [
            "schema",
            "column",
            "datatype",
        ],
        Intent.STATISTICS: [
            "statistics",
            "mean",
            "median",
            "average",
            "describe",
        ],
        Intent.CORRELATION: [
            "correlation",
            "relationship",
        ],
        Intent.DISTRIBUTION: [
            "distribution",
            "histogram",
        ],
        Intent.OUTLIER: [
            "outlier",
            "anomaly value",
        ],
        Intent.QUALITY: [
            "quality",
            "clean",
        ],
        Intent.HEALTH: [
            "health",
        ],
        Intent.INSIGHT: [
            "insight",
            "findings",
        ],
        Intent.KPI: [
            "kpi",
            "metric",
        ],
        Intent.SUMMARY: [
            "summary",
        ],
        Intent.VISUALIZATION: [
            "chart",
            "graph",
            "plot",
            "visualization",
        ],
        Intent.FORECAST: [
            "forecast",
            "predict future",
        ],
        Intent.TREND: [
            "trend",
        ],
        Intent.TIMESERIES: [
            "time series",
            "timeseries",
        ],
        Intent.ANOMALY: [
            "anomaly",
        ],
        Intent.DASHBOARD: [
            "dashboard",
        ],
        Intent.REPORT: [
            "report",
        ],
        Intent.AUTOML: [
            "automl",
            "model",
        ],
        Intent.REGRESSION: [
            "regression",
        ],
        Intent.CLASSIFICATION: [
            "classification",
            "classify",
        ],
        Intent.CLUSTERING: [
            "cluster",
            "clustering",
        ],
    }

    @classmethod
    def detect(cls, query: str) -> list[Intent]:

        query = query.lower()

        intents = []

        for intent, words in cls.KEYWORDS.items():

            if any(word in query for word in words):

                intents.append(intent)

        if not intents:

            intents.append(Intent.UNKNOWN)

        return intents