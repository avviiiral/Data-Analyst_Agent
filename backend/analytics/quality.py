from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class QualityIssue:
    column: str
    issue: str
    severity: str
    recommendation: str


@dataclass
class QualityReport:
    score: int
    issues: list[QualityIssue] = field(default_factory=list)


class DataQualityAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> QualityReport:

        df = dataset.dataframe

        score = 100

        issues: list[QualityIssue] = []

        for column in df.columns:

            series = df[column]

            missing = series.isna().mean() * 100

            if missing > 0:

                score -= min(int(missing), 20)

                issues.append(
                    QualityIssue(
                        column=column,
                        issue=f"{missing:.2f}% Missing Values",
                        severity="High" if missing > 20 else "Medium",
                        recommendation="Fill or remove missing values.",
                    )
                )

            if series.nunique(dropna=False) == 1:

                score -= 5

                issues.append(
                    QualityIssue(
                        column=column,
                        issue="Constant Column",
                        severity="Low",
                        recommendation="Consider dropping this column.",
                    )
                )

            if (
                pd.api.types.is_object_dtype(series)
                or pd.api.types.is_categorical_dtype(series)
            ):

                cardinality = series.nunique() / max(len(series), 1)

                if cardinality > 0.90:

                    issues.append(
                        QualityIssue(
                            column=column,
                            issue="High Cardinality",
                            severity="Low",
                            recommendation="May not be useful for grouping.",
                        )
                    )

        duplicates = int(df.duplicated().sum())

        if duplicates > 0:

            score -= min(duplicates * 2, 20)

            issues.append(
                QualityIssue(
                    column="-",
                    issue=f"{duplicates} Duplicate Rows",
                    severity="Medium",
                    recommendation="Remove duplicate rows.",
                )
            )

        score = max(score, 0)

        return QualityReport(
            score=score,
            issues=issues,
        )