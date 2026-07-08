import pandas as pd


class InsightGenerator:
    def generate(self, dataframe: pd.DataFrame):
        return {
            "rows": int(len(dataframe)),
            "columns": int(len(dataframe.columns)),
            "missing_values": int(dataframe.isna().sum().sum()),
            "duplicates": int(dataframe.duplicated().sum()),
        }