from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class OutlierInfo:
    column: str
    outlier_count: int
    outlier_percentage: float
    lower_bound: float
    upper_bound: float
    outlier_indices: list[int] = field(default_factory=list)


@dataclass
class OutlierReport:
    columns: list[OutlierInfo] = field(default_factory=list)


class OutlierAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> OutlierReport:

        df = dataset.dataframe

        report = OutlierReport()

        numeric_df = df.select_dtypes(include="number")

        for column in numeric_df.columns:

            series = numeric_df[column]

            q1 = series.quantile(0.25)
            q3 = series.quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            mask = (series < lower) | (series > upper)

            indices = series[mask].index.tolist()

            report.columns.append(
                OutlierInfo(
                    column=column,
                    outlier_count=len(indices),
                    outlier_percentage=round(
                        len(indices) / max(len(series), 1) * 100,
                        2,
                    ),
                    lower_bound=round(float(lower), 4),
                    upper_bound=round(float(upper), 4),
                    outlier_indices=indices,
                )
            )

        return report