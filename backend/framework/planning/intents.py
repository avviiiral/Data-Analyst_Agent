from __future__ import annotations

from enum import Enum


class Intent(str, Enum):

    PROFILE = "profile"

    SCHEMA = "schema"

    STATISTICS = "statistics"

    CORRELATION = "correlation"

    DISTRIBUTION = "distribution"

    OUTLIER = "outlier"

    QUALITY = "quality"

    HEALTH = "health"

    INSIGHT = "insight"

    KPI = "kpi"

    SUMMARY = "summary"

    VISUALIZATION = "visualization"

    FORECAST = "forecast"

    TREND = "trend"

    TIMESERIES = "timeseries"

    ANOMALY = "anomaly"

    DASHBOARD = "dashboard"

    REPORT = "report"

    AUTOML = "automl"

    REGRESSION = "regression"

    CLASSIFICATION = "classification"

    CLUSTERING = "clustering"

    UNKNOWN = "unknown"