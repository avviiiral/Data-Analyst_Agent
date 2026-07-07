from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class DistributionInfo:
    column: str

    minimum: float
    maximum: float

    q1: float
    median: float
    q3: float

    iqr: float

    skewness: float
    kurtosis: float

    distribution: str


@dataclass
class DistributionReport:
    columns: list[DistributionInfo] = field(default_factory=list)


class DistributionAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> DistributionReport:

        df = dataset.dataframe

        report = DistributionReport()

        numeric = df.select_dtypes(include="number")

        for column in numeric.columns:

            s = numeric[column]

            skew = float(s.skew())
            kurt = float(s.kurtosis())

            if abs(skew) < 0.5:
                dist = "Approximately Normal"

            elif skew > 0.5:
                dist = "Right Skewed"

            else:
                dist = "Left Skewed"

            q1 = float(s.quantile(0.25))
            median = float(s.quantile(0.50))
            q3 = float(s.quantile(0.75))

            report.columns.append(
                DistributionInfo(
                    column=column,
                    minimum=round(float(s.min()), 4),
                    maximum=round(float(s.max()), 4),
                    q1=round(q1, 4),
                    median=round(median, 4),
                    q3=round(q3, 4),
                    iqr=round(q3 - q1, 4),
                    skewness=round(skew, 4),
                    kurtosis=round(kurt, 4),
                    distribution=dist,
                )
            )

        return report