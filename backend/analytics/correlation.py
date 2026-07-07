from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class CorrelationPair:
    feature_1: str
    feature_2: str
    correlation: float
    strength: str


@dataclass
class CorrelationReport:
    matrix: pd.DataFrame
    pairs: list[CorrelationPair] = field(default_factory=list)


class CorrelationAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> CorrelationReport:

        numeric = dataset.dataframe.select_dtypes(include="number")

        matrix = numeric.corr(numeric_only=True)

        report = CorrelationReport(matrix=matrix)

        columns = list(matrix.columns)

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):

                value = float(matrix.iloc[i, j])

                abs_value = abs(value)

                if abs_value >= 0.90:
                    strength = "Very Strong"

                elif abs_value >= 0.70:
                    strength = "Strong"

                elif abs_value >= 0.50:
                    strength = "Moderate"

                elif abs_value >= 0.30:
                    strength = "Weak"

                else:
                    strength = "Very Weak"

                report.pairs.append(
                    CorrelationPair(
                        feature_1=columns[i],
                        feature_2=columns[j],
                        correlation=round(value, 4),
                        strength=strength,
                    )
                )

        report.pairs.sort(
            key=lambda x: abs(x.correlation),
            reverse=True,
        )

        return report