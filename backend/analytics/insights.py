from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class Insight:
    title: str
    description: str
    severity: str
    recommendation: str


@dataclass
class InsightReport:
    insights: list[Insight] = field(default_factory=list)


class InsightAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> InsightReport:

        df = dataset.dataframe

        report = InsightReport()

        numeric = df.select_dtypes(include="number")

        if numeric.empty:

            report.insights.append(
                Insight(
                    title="No Numeric Columns",
                    description="Statistical insights cannot be generated.",
                    severity="Info",
                    recommendation="Upload a dataset containing numeric columns.",
                )
            )

            return report

        # Missing values
        missing = int(df.isna().sum().sum())

        if missing == 0:
            report.insights.append(
                Insight(
                    title="Excellent Data Quality",
                    description="No missing values detected.",
                    severity="Positive",
                    recommendation="No action required.",
                )
            )

        # Duplicate rows
        duplicates = int(df.duplicated().sum())

        if duplicates == 0:
            report.insights.append(
                Insight(
                    title="No Duplicate Records",
                    description="Dataset contains no duplicate rows.",
                    severity="Positive",
                    recommendation="No action required.",
                )
            )

        # Highly correlated columns
        corr = numeric.corr(numeric_only=True)

        cols = corr.columns.tolist()

        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):

                value = abs(corr.iloc[i, j])

                if value >= 0.90:

                    report.insights.append(
                        Insight(
                            title="Strong Correlation",
                            description=f"{cols[i]} and {cols[j]} have correlation of {value:.2f}.",
                            severity="Info",
                            recommendation="Check for multicollinearity before building ML models.",
                        )
                    )

        # High cardinality
        for column in df.select_dtypes(include=["object", "category"]).columns:

            ratio = df[column].nunique() / max(len(df), 1)

            if ratio > 0.90:

                report.insights.append(
                    Insight(
                        title="High Cardinality",
                        description=f"{column} contains mostly unique values.",
                        severity="Info",
                        recommendation="Avoid using it as a grouping column.",
                    )
                )

        # Numeric spread
        for column in numeric.columns:

            std = float(numeric[column].std())
            mean = float(numeric[column].mean())

            if mean != 0 and std / abs(mean) > 1:

                report.insights.append(
                    Insight(
                        title="High Variability",
                        description=f"{column} has high variability.",
                        severity="Info",
                        recommendation="Consider normalization before ML.",
                    )
                )

        return report