import pandas as pd


class KPIService:
    def generate(self, dataframe: pd.DataFrame):
        numeric = dataframe.select_dtypes(include="number")

        return {
            "total_rows": len(dataframe),
            "total_columns": len(dataframe.columns),
            "numeric_columns": len(numeric.columns),
            "sum": numeric.sum().to_dict(),
            "average": numeric.mean().to_dict(),
        }