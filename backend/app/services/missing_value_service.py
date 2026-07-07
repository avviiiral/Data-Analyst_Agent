import pandas as pd


class MissingValueService:
    def analyze(self, dataframe: pd.DataFrame):
        return dataframe.isna().sum().to_dict()