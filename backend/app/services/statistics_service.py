import pandas as pd


class StatisticsService:
    def summary(self, dataframe: pd.DataFrame):
        summary = dataframe.describe(include="all").fillna("")

        result = {}

        for column in summary.columns:
            result[column] = {}

            for index, value in summary[column].items():
                if hasattr(value, "item"):
                    value = value.item()

                result[column][str(index)] = value

        return result