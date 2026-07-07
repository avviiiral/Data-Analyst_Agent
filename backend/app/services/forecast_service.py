import pandas as pd
from sklearn.linear_model import LinearRegression


class ForecastService:
    def forecast(
        self,
        dataframe: pd.DataFrame,
        date_column: str,
        value_column: str,
        periods: int = 5,
    ):
        df = dataframe[[date_column, value_column]].copy()

        df[date_column] = pd.to_datetime(df[date_column])

        df = df.sort_values(date_column)

        df["index"] = range(len(df))

        model = LinearRegression()

        model.fit(
            df[["index"]],
            df[value_column],
        )

        future = pd.DataFrame(
            {
                "index": range(
                    len(df),
                    len(df) + periods,
                )
            }
        )

        prediction = model.predict(future)

        return prediction.tolist()