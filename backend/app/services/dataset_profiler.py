import pandas as pd


class DatasetProfiler:
    def profile(self, dataframe: pd.DataFrame):
        return {
            "rows": len(dataframe),
            "columns": len(dataframe.columns),
            "column_names": dataframe.columns.tolist(),
            "data_types": {
                column: str(dtype)
                for column, dtype in dataframe.dtypes.items()
            },
            "missing_values": dataframe.isnull().sum().to_dict(),
            "duplicate_rows": int(dataframe.duplicated().sum()),
            "memory_usage_mb": round(
                dataframe.memory_usage(deep=True).sum() / 1024 / 1024,
                2,
            ),
        }