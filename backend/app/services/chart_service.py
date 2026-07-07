import pandas as pd
import plotly.express as px


class ChartService:
    def bar(self, dataframe: pd.DataFrame, x: str, y: str):
        return px.bar(dataframe, x=x, y=y)

    def line(self, dataframe: pd.DataFrame, x: str, y: str):
        return px.line(dataframe, x=x, y=y)

    def scatter(self, dataframe: pd.DataFrame, x: str, y: str):
        return px.scatter(dataframe, x=x, y=y)

    def histogram(self, dataframe: pd.DataFrame, column: str):
        return px.histogram(dataframe, x=column)