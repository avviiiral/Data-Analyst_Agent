import pandas as pd


class ChartRecommender:
    def recommend(self, dataframe: pd.DataFrame):
        recommendations = {}

        for column in dataframe.columns:
            dtype = str(dataframe[column].dtype)

            if "int" in dtype or "float" in dtype:
                recommendations[column] = "Histogram"

            else:
                recommendations[column] = "Bar Chart"

        return recommendations