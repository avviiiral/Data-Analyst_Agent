import pandas as pd


class DashboardBuilder:
    def build(self, dataframe: pd.DataFrame):
        return {
            "total_rows": len(dataframe),
            "total_columns": len(dataframe.columns),
            "charts": [
                "Bar Chart",
                "Line Chart",
                "Pie Chart",
                "Scatter Plot",
                "Histogram",
            ],
        }