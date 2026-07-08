import pandas as pd


class DatasetProfiler:
    def profile(self, dataframe: pd.DataFrame):
        return {
            "rows": int(len(dataframe)),
            "columns": int(len(dataframe.columns)),
            "column_names": dataframe.columns.tolist(),
            "data_types": {
                column: str(dtype)
                for column, dtype in dataframe.dtypes.items()
            },
            "missing_values": {
                column: int(value)
                for column, value in dataframe.isnull().sum().items()
            },
            "duplicate_rows": int(dataframe.duplicated().sum()),
            "memory_usage_mb": float(
                round(
                    dataframe.memory_usage(deep=True).sum()
                    / 1024
                    / 1024,
                    2,
                )
            ),
        }