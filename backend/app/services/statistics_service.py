import pandas as pd


class StatisticsService:
    def summary(self, dataframe: pd.DataFrame):
        return dataframe.describe(include="all").fillna("").to_dict()