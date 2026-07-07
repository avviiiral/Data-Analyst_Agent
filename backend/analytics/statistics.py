from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class NumericStatistics:
    column: str

    count: int
    mean: float
    median: float
    mode: float | int | str | None

    minimum: float
    maximum: float
    range: float

    variance: float
    std: float

    q1: float
    q3: float
    iqr: float

    skewness: float
    kurtosis: float

    sum: float


@dataclass
class StatisticsReport:
    statistics: list[NumericStatistics] = field(default_factory=list)


class StatisticsAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> StatisticsReport:

        df = dataset.dataframe

        report = StatisticsReport()

        numeric_df = df.select_dtypes(include="number")

        for column in numeric_df.columns:

            s = numeric_df[column]

            mode = s.mode()

            report.statistics.append(
                NumericStatistics(
                    column=column,
                    count=int(s.count()),
                    mean=round(float(s.mean()), 4),
                    median=round(float(s.median()), 4),
                    mode=None if mode.empty else mode.iloc[0],
                    minimum=round(float(s.min()), 4),
                    maximum=round(float(s.max()), 4),
                    range=round(float(s.max() - s.min()), 4),
                    variance=round(float(s.var()), 4),
                    std=round(float(s.std()), 4),
                    q1=round(float(s.quantile(0.25)), 4),
                    q3=round(float(s.quantile(0.75)), 4),
                    iqr=round(
                        float(
                            s.quantile(0.75)
                            - s.quantile(0.25)
                        ),
                        4,
                    ),
                    skewness=round(float(s.skew()), 4),
                    kurtosis=round(float(s.kurtosis()), 4),
                    sum=round(float(s.sum()), 4),
                )
            )

        return report