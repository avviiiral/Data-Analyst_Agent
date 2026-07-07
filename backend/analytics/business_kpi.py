from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class KPI:
    name: str
    value: object
    description: str


@dataclass
class KPIReport:
    kpis: list[KPI] = field(default_factory=list)


class BusinessKPIAnalyzer:

    @staticmethod
    def analyze(dataset: Dataset) -> KPIReport:

        df = dataset.dataframe

        report = KPIReport()

        report.kpis.append(
            KPI(
                name="Total Records",
                value=len(df),
                description="Total number of rows.",
            )
        )

        report.kpis.append(
            KPI(
                name="Total Columns",
                value=len(df.columns),
                description="Total number of columns.",
            )
        )

        report.kpis.append(
            KPI(
                name="Missing Values",
                value=int(df.isna().sum().sum()),
                description="Total missing values.",
            )
        )

        report.kpis.append(
            KPI(
                name="Duplicate Rows",
                value=int(df.duplicated().sum()),
                description="Duplicate records.",
            )
        )

        numeric = df.select_dtypes(include="number")

        for column in numeric.columns:

            report.kpis.append(
                KPI(
                    name=f"{column} Sum",
                    value=round(float(numeric[column].sum()), 2),
                    description=f"Total of {column}",
                )
            )

            report.kpis.append(
                KPI(
                    name=f"{column} Average",
                    value=round(float(numeric[column].mean()), 2),
                    description=f"Average of {column}",
                )
            )

            report.kpis.append(
                KPI(
                    name=f"{column} Maximum",
                    value=round(float(numeric[column].max()), 2),
                    description=f"Maximum {column}",
                )
            )

            report.kpis.append(
                KPI(
                    name=f"{column} Minimum",
                    value=round(float(numeric[column].min()), 2),
                    description=f"Minimum {column}",
                )
            )

        return report