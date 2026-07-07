from dataclasses import dataclass, field

import pandas as pd

from backend.datasets.dataset import Dataset


@dataclass
class ColumnProfile:
    name: str
    dtype: str

    missing: int
    missing_percent: float

    unique: int

    minimum: object = None
    maximum: object = None
    mean: object = None
    median: object = None
    std: object = None

    sample_values: list = field(default_factory=list)


@dataclass
class DatasetProfile:
    rows: int
    columns: int

    numeric_columns: int
    categorical_columns: int
    datetime_columns: int

    columns_profile: list[ColumnProfile] = field(default_factory=list)


class DataProfiler:

    @staticmethod
    def profile(dataset: Dataset) -> DatasetProfile:

        df = dataset.dataframe

        profile = DatasetProfile(
            rows=len(df),
            columns=len(df.columns),
            numeric_columns=0,
            categorical_columns=0,
            datetime_columns=0,
        )

        for column in df.columns:

            series = df[column]

            dtype = str(series.dtype)

            info = ColumnProfile(
                name=column,
                dtype=dtype,
                missing=int(series.isna().sum()),
                missing_percent=round(
                    series.isna().mean() * 100,
                    2,
                ),
                unique=int(series.nunique(dropna=True)),
                sample_values=series.dropna().head(5).tolist(),
            )

            if pd.api.types.is_numeric_dtype(series):

                profile.numeric_columns += 1

                info.minimum = float(series.min())

                info.maximum = float(series.max())

                info.mean = round(float(series.mean()), 2)

                info.median = round(float(series.median()), 2)

                info.std = round(float(series.std()), 2)

            elif pd.api.types.is_datetime64_any_dtype(series):

                profile.datetime_columns += 1

                info.minimum = str(series.min())

                info.maximum = str(series.max())

            else:

                profile.categorical_columns += 1

            profile.columns_profile.append(info)

        return profile