import pandas as pd
from sklearn.linear_model import LinearRegression


class ForecastService:

    def forecast(
        self,
        dataframe: pd.DataFrame,
        periods: int = 6,
    ):

        date_column = None
        value_column = None

        # Detect date column
        for column in dataframe.columns:
            if pd.api.types.is_datetime64_any_dtype(dataframe[column]):
                date_column = column
                break

        if date_column is None:
            raise ValueError("No datetime column found.")

        # Detect numeric value column
        numeric_columns = dataframe.select_dtypes(include="number").columns.tolist()

        if not numeric_columns:
            raise ValueError("No numeric column found.")

        value_column = numeric_columns[-1]

        df = dataframe[[date_column, value_column]].dropna().copy()

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

        predictions = model.predict(future)

        future_dates = pd.date_range(
            start=df[date_column].max(),
            periods=periods + 1,
            freq="MS",
        )[1:]

        return [
            {
                "date": date.strftime("%Y-%m-%d"),
                "prediction": float(value),
            }
            for date, value in zip(
                future_dates,
                predictions,
            )
        ]