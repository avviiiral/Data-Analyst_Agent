import pandas as pd


class InsightGenerator:
    def generate(self, dataframe: pd.DataFrame):
        return {
            "rows": len(dataframe),
            "columns": len(dataframe.columns),
            "missing_values": dataframe.isna().sum().sum(),
            "duplicates": int(dataframe.duplicated().sum()),
        }