from dataclasses import dataclass

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class ExecutiveSummary:
    dataset_name: str
    rows: int
    columns: int

    numeric_columns: int
    categorical_columns: int
    datetime_columns: int

    missing_values: int
    duplicate_rows: int

    overall_health: str

    summary: str


class ExecutiveSummaryGenerator:

    @staticmethod
    def generate(dataset: Dataset) -> ExecutiveSummary:

        df = dataset.dataframe

        rows = len(df)
        columns = len(df.columns)

        numeric = len(df.select_dtypes(include="number").columns)

        categorical = len(
            df.select_dtypes(
                include=["object", "category"]
            ).columns
        )

        datetime = len(
            df.select_dtypes(
                include=["datetime"]
            ).columns
        )

        missing = int(df.isna().sum().sum())

        duplicates = int(df.duplicated().sum())

        score = 100

        score -= min(missing, 20)

        score -= min(duplicates * 2, 20)

        if score >= 90:
            health = "Excellent"

        elif score >= 75:
            health = "Good"

        elif score >= 60:
            health = "Average"

        else:
            health = "Poor"

        summary = (
            f"The dataset contains {rows:,} rows and "
            f"{columns} columns. "
            f"It has {numeric} numeric, "
            f"{categorical} categorical and "
            f"{datetime} datetime columns. "
            f"There are {missing} missing values and "
            f"{duplicates} duplicate rows. "
            f"Overall dataset health is rated as {health}."
        )

        return ExecutiveSummary(
            dataset_name=dataset.name,
            rows=rows,
            columns=columns,
            numeric_columns=numeric,
            categorical_columns=categorical,
            datetime_columns=datetime,
            missing_values=missing,
            duplicate_rows=duplicates,
            overall_health=health,
            summary=summary,
        )