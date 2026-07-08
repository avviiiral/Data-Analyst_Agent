import pandas as pd


class CorrelationService:
    def correlation(self, dataframe: pd.DataFrame):
        numeric = dataframe.select_dtypes(include="number")

        if numeric.empty:
            return {}

        corr = numeric.corr().fillna(0)

        result = {}

        for column in corr.columns:
            result[column] = {}

            for index, value in corr[column].items():
                result[column][index] = float(value)

        return result