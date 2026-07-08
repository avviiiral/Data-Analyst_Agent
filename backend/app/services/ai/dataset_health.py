import pandas as pd


class DatasetHealth:
    def score(self, dataframe: pd.DataFrame):
        missing = int(dataframe.isna().sum().sum())

        duplicates = int(dataframe.duplicated().sum())

        score = 100 - missing - duplicates

        return int(max(score, 0))