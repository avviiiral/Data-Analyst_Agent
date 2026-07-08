from pathlib import Path

import pandas as pd


class DatasetLoader:

    def load(self, path: str) -> pd.DataFrame:
        extension = Path(path).suffix.lower()

        if extension == ".csv":
            dataframe = pd.read_csv(
                path,
                engine="python",
            )

        elif extension in [".xlsx", ".xls"]:
            dataframe = self._load_excel(path)

        elif extension == ".json":
            dataframe = pd.read_json(path)

        elif extension == ".parquet":
            dataframe = pd.read_parquet(path)

        else:
            raise ValueError("Unsupported dataset.")

        dataframe = self._clean_dataframe(dataframe)

        return dataframe

    def _load_excel(self, path: str) -> pd.DataFrame:
        preview = pd.read_excel(
            path,
            header=None,
            nrows=20,
        )

        header_row = 0
        best_score = -1

        for i in range(len(preview)):
            score = preview.iloc[i].notna().sum()

            if score > best_score:
                best_score = score
                header_row = i

        return pd.read_excel(
            path,
            header=header_row,
        )

    def _clean_dataframe(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        dataframe.columns = [
            str(column).strip()
            for column in dataframe.columns
        ]

        dataframe = dataframe.dropna(
            how="all"
        )

        dataframe = dataframe.dropna(
            axis=1,
            how="all"
        )

        dataframe = dataframe.loc[
            :,
            ~dataframe.columns.str.startswith("Unnamed"),
        ]

        dataframe = dataframe.reset_index(
            drop=True
        )

        for column in dataframe.columns:

            dataframe[column] = dataframe[column].replace(
                "",
                pd.NA,
            )

            column_name = column.lower()

            # Parse date columns FIRST
            if any(
                keyword in column_name
                for keyword in [
                    "date",
                    "month",
                    "year",
                    "time",
                    "day",
                ]
            ):
                dates = pd.to_datetime(
                    dataframe[column],
                    errors="coerce",
                )

                if dates.notna().sum() >= len(dataframe) * 0.8:
                    dataframe[column] = dates
                    continue

            # Parse numeric columns
            numeric = pd.to_numeric(
                dataframe[column],
                errors="coerce",
            )

            if numeric.notna().sum() >= len(dataframe) * 0.8:
                dataframe[column] = numeric
                continue

            # Convert low-cardinality object columns to category
            if dataframe[column].dtype == "object":
                unique_ratio = (
                    dataframe[column].nunique(dropna=True)
                    / max(len(dataframe), 1)
                )

                if unique_ratio < 0.5:
                    dataframe[column] = dataframe[column].astype("category")

        return dataframe