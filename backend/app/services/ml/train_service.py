import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class TrainService:
    def train(
        self,
        dataframe: pd.DataFrame,
        target: str,
    ):
        x = dataframe.drop(columns=[target])

        x = pd.get_dummies(x)

        y = dataframe[target]

        model = RandomForestClassifier(
            random_state=42,
        )

        model.fit(x, y)

        return model