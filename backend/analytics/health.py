from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class HealthIssue:
    category: str
    severity: str
    column: str
    message: str


@dataclass
class DatasetHealth:
    score: int
    issues: list[HealthIssue] = field(default_factory=list)


class DatasetHealthAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> DatasetHealth:

        df = dataset.dataframe

        score = 100

        issues: list[HealthIssue] = []

        # Missing Values
        for column in df.columns:

            missing = df[column].isna().mean() * 100

            if missing > 0:

                deduction = min(int(missing), 20)

                score -= deduction

                issues.append(
                    HealthIssue(
                        category="Missing Values",
                        severity="High" if missing > 20 else "Medium",
                        column=column,
                        message=f"{missing:.2f}% missing values",
                    )
                )

        # Duplicate Rows
        duplicates = int(df.duplicated().sum())

        if duplicates:

            score -= min(duplicates * 2, 20)

            issues.append(
                HealthIssue(
                    category="Duplicates",
                    severity="Medium",
                    column="-",
                    message=f"{duplicates} duplicate rows found",
                )
            )

        # Constant Columns
        for column in df.columns:

            if df[column].nunique(dropna=False) == 1:

                score -= 5

                issues.append(
                    HealthIssue(
                        category="Constant Column",
                        severity="Low",
                        column=column,
                        message="Only one unique value",
                    )
                )

        # High Cardinality
        for column in df.select_dtypes(include=["object", "category"]).columns:

            ratio = df[column].nunique() / max(len(df), 1)

            if ratio > 0.90:

                issues.append(
                    HealthIssue(
                        category="High Cardinality",
                        severity="Low",
                        column=column,
                        message="Nearly every value is unique",
                    )
                )

        score = max(score, 0)

        return DatasetHealth(
            score=score,
            issues=issues,
        )