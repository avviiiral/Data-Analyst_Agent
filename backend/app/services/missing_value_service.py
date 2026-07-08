import pandas as pd


class MissingValueService:
    def analyze(self, dataframe: pd.DataFrame):
        return {
            column: int(value)
            for column, value in dataframe.isna().sum().items()
        }