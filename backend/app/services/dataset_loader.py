from pathlib import Path

import pandas as pd


class DatasetLoader:
    def load(self, path: str):
        extension = Path(path).suffix.lower()

        if extension == ".csv":
            return pd.read_csv(path)

        if extension in [".xlsx", ".xls"]:
            return pd.read_excel(path)

        if extension == ".json":
            return pd.read_json(path)

        if extension == ".parquet":
            return pd.read_parquet(path)

        raise ValueError("Unsupported dataset.")