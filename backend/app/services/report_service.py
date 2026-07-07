import pandas as pd


class ReportService:
    def generate(self, dataframe: pd.DataFrame):
        return {
            "shape": dataframe.shape,
            "columns": dataframe.columns.tolist(),
            "missing_values": dataframe.isna().sum().to_dict(),
        }