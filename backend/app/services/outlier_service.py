import pandas as pd


class OutlierService:
    def detect(self, dataframe: pd.DataFrame):
        numeric = dataframe.select_dtypes(include="number")

        result = {}

        for column in numeric.columns:
            q1 = numeric[column].quantile(0.25)
            q3 = numeric[column].quantile(0.75)

            iqr = q3 - q1

            outliers = numeric[
                (numeric[column] < q1 - 1.5 * iqr)
                | (numeric[column] > q3 + 1.5 * iqr)
            ]

            result[column] = len(outliers)

        return result