import pandas as pd


class RecommendationEngine:
    def recommend(self, dataframe: pd.DataFrame):
        recommendations = []

        if dataframe.isna().sum().sum() > 0:
            recommendations.append(
                "Dataset contains missing values."
            )

        if dataframe.duplicated().sum() > 0:
            recommendations.append(
                "Dataset contains duplicate rows."
            )

        return recommendations