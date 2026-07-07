import pandas as pd


class InsightService:
    def generate(self, dataframe: pd.DataFrame):
        return {
            "rows": len(dataframe),
            "columns": len(dataframe.columns),
            "numeric_columns": dataframe.select_dtypes(
                include="number"
            ).columns.tolist(),
            "categorical_columns": dataframe.select_dtypes(
                exclude="number"
            ).columns.tolist(),
        }