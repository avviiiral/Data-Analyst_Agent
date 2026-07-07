import pandas as pd


class CorrelationService:
    def correlation(self, dataframe: pd.DataFrame):
        numeric = dataframe.select_dtypes(include=["number"])

        if numeric.empty:
            return {}

        return numeric.corr().fillna(0).to_dict()