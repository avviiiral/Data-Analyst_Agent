import pandas as pd


class DatasetHealth:
    def score(self, dataframe: pd.DataFrame):
        missing = dataframe.isna().sum().sum()

        duplicates = dataframe.duplicated().sum()

        score = 100

        score -= int(missing)

        score -= int(duplicates)

        return max(score, 0)