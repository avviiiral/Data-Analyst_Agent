from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class Recommendation:
    priority: str
    category: str
    recommendation: str
    reason: str


@dataclass
class RecommendationReport:
    recommendations: list[Recommendation] = field(default_factory=list)


class RecommendationEngine:

    @staticmethod
    def analyze(dataset: Dataset) -> RecommendationReport:

        df = dataset.dataframe

        report = RecommendationReport()

        # Missing values
        if df.isna().sum().sum() > 0:
            report.recommendations.append(
                Recommendation(
                    priority="High",
                    category="Data Cleaning",
                    recommendation="Handle missing values before analysis.",
                    reason="Missing values reduce analysis quality.",
                )
            )

        # Duplicate rows
        duplicates = int(df.duplicated().sum())

        if duplicates > 0:
            report.recommendations.append(
                Recommendation(
                    priority="High",
                    category="Data Cleaning",
                    recommendation="Remove duplicate rows.",
                    reason=f"{duplicates} duplicate rows detected.",
                )
            )

        # Numeric data
        numeric = df.select_dtypes(include="number")

        if len(numeric.columns) >= 2:
            report.recommendations.append(
                Recommendation(
                    priority="Medium",
                    category="Analytics",
                    recommendation="Generate a correlation heatmap.",
                    reason="Multiple numeric columns are available.",
                )
            )

        if len(numeric.columns) >= 1:
            report.recommendations.append(
                Recommendation(
                    priority="Medium",
                    category="Analytics",
                    recommendation="Run outlier detection.",
                    reason="Numeric columns detected.",
                )
            )

        # Datetime columns
        datetime_cols = df.select_dtypes(
            include=["datetime"]
        )

        if len(datetime_cols.columns) > 0:
            report.recommendations.append(
                Recommendation(
                    priority="Medium",
                    category="Forecasting",
                    recommendation="Generate trend and forecasting analysis.",
                    reason="Datetime column detected.",
                )
            )

        # Categorical columns
        categorical = df.select_dtypes(
            include=["object", "category"]
        )

        if len(categorical.columns) > 0:
            report.recommendations.append(
                Recommendation(
                    priority="Low",
                    category="Visualization",
                    recommendation="Create category-wise comparison charts.",
                    reason="Categorical columns available.",
                )
            )

        # Dataset size
        if len(df) > 10000:
            report.recommendations.append(
                Recommendation(
                    priority="Low",
                    category="Performance",
                    recommendation="Enable lazy loading and sampling.",
                    reason="Large dataset detected.",
                )
            )

        return report