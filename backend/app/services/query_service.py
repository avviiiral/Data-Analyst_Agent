import pandas as pd


class QueryService:
    def execute(self, dataframe: pd.DataFrame, query: str):
        query = query.lower()

        if "rows" in query:
            return len(dataframe)

        if "columns" in query:
            return len(dataframe.columns)

        return "Query not supported."