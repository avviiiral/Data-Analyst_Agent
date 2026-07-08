import re

import pandas as pd


class SchemaDetector:

    def detect(self, dataframe: pd.DataFrame):
        schema = []

        for column in dataframe.columns:

            dtype = str(dataframe[column].dtype)

            semantic_type = self._semantic_type(
                column,
                dataframe[column],
            )

            schema.append(
                {
                    "column": column,
                    "dtype": dtype,
                    "semantic_type": semantic_type,
                    "nullable": bool(dataframe[column].isna().any()),
                    "unique": bool(dataframe[column].is_unique),
                }
            )

        return schema

    def _semantic_type(
        self,
        column: str,
        series: pd.Series,
    ) -> str:

        name = column.lower()

        if pd.api.types.is_datetime64_any_dtype(series):
            return "datetime"

        if pd.api.types.is_bool_dtype(series):
            return "boolean"

        if pd.api.types.is_numeric_dtype(series):

            if any(
                keyword in name
                for keyword in [
                    "price",
                    "amount",
                    "cost",
                    "revenue",
                    "salary",
                    "income",
                    "profit",
                    "sales",
                    "tax",
                    "expense",
                ]
            ):
                return "currency"

            if any(
                keyword in name
                for keyword in [
                    "id",
                    "code",
                    "number",
                    "no",
                ]
            ):
                return "identifier"

            return "numeric"

        if any(
            keyword in name
            for keyword in [
                "email",
                "mail",
            ]
        ):
            return "email"

        if any(
            keyword in name
            for keyword in [
                "phone",
                "mobile",
                "contact",
            ]
        ):
            return "phone"

        if any(
            keyword in name
            for keyword in [
                "country",
            ]
        ):
            return "country"

        if any(
            keyword in name
            for keyword in [
                "city",
            ]
        ):
            return "city"

        if any(
            keyword in name
            for keyword in [
                "state",
            ]
        ):
            return "state"

        if any(
            keyword in name
            for keyword in [
                "zip",
                "postal",
                "pincode",
            ]
        ):
            return "postal_code"

        if any(
            keyword in name
            for keyword in [
                "name",
                "customer",
                "employee",
                "person",
            ]
        ):
            return "name"

        if any(
            keyword in name
            for keyword in [
                "category",
                "type",
                "group",
            ]
        ):
            return "category"

        sample = series.dropna().astype(str).head(10)

        if not sample.empty:

            if all(
                re.match(r"^https?://", value)
                for value in sample
            ):
                return "url"

        return "text"