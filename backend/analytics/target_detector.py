from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class TargetCandidate:
    column: str
    score: float
    reason: str
    problem_type: str


@dataclass
class TargetDetectionReport:
    best_target: TargetCandidate | None
    candidates: list[TargetCandidate] = field(default_factory=list)


class TargetDetector:
    """
    Detect the most likely target column for ML.
    """

    REGRESSION_KEYWORDS = {
        "sales",
        "profit",
        "price",
        "amount",
        "cost",
        "revenue",
        "income",
        "salary",
        "value",
        "score",
        "quantity",
        "target",
    }

    CLASSIFICATION_KEYWORDS = {
        "class",
        "label",
        "status",
        "result",
        "grade",
        "segment",
        "risk",
        "approved",
        "rejected",
        "fraud",
        "default",
        "churn",
    }

    ID_KEYWORDS = {
        "id",
        "uuid",
        "code",
        "number",
        "serial",
        "sr",
    }

    @staticmethod
    def analyze(dataset: Dataset) -> TargetDetectionReport:

        df = dataset.dataframe

        report = TargetDetectionReport(best_target=None)

        for column in df.columns:

            series = df[column]

            score = 0.0

            reasons = []

            name = column.lower()

            # Ignore identifier columns
            if any(word in name for word in TargetDetector.ID_KEYWORDS):
                score -= 100
                reasons.append("identifier")

            # Numeric columns
            if pd.api.types.is_numeric_dtype(series):

                score += 30
                problem = "Regression"

                reasons.append("numeric")

                if any(k in name for k in TargetDetector.REGRESSION_KEYWORDS):
                    score += 50
                    reasons.append("business_metric")

                unique_ratio = series.nunique() / max(len(series), 1)

                # Penalize almost unique numeric columns
                if unique_ratio > 0.95:
                    score -= 30
                    reasons.append("high_cardinality")

            else:

                unique = series.nunique()

                problem = "Classification"

                # Ideal class count
                if 2 <= unique <= 20:
                    score += 40
                    reasons.append("reasonable_classes")

                elif unique > 100:
                    score -= 30
                    reasons.append("too_many_classes")

                if any(k in name for k in TargetDetector.CLASSIFICATION_KEYWORDS):
                    score += 40
                    reasons.append("classification_keyword")

            report.candidates.append(
                TargetCandidate(
                    column=column,
                    score=round(score, 2),
                    reason=", ".join(reasons),
                    problem_type=problem,
                )
            )

        report.candidates.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        if report.candidates:
            report.best_target = report.candidates[0]

        return report