import pandas as pd


class PredictService:
    def predict(
        self,
        model,
        dataframe: pd.DataFrame,
    ):
        dataframe = pd.get_dummies(dataframe)

        return model.predict(dataframe).tolist()