from typing import Dict

import pandas as pd

from backend.datasets.dataset import Dataset


class DatasetRegistry:

    _datasets: Dict[str, Dataset] = {}

    @classmethod
    def add(
        cls,
        dataset_id: str,
        dataframe: pd.DataFrame,
        name: str = "",
        path: str = "",
    ):

        dataset = Dataset.from_dataframe(
            dataframe=dataframe,
            dataset_id=dataset_id,
            name=name,
            path=path,
        )

        cls._datasets[dataset_id] = dataset

    @classmethod
    def get(
        cls,
        dataset_id: str,
    ) -> Dataset | None:

        return cls._datasets.get(dataset_id)

    @classmethod
    def exists(
        cls,
        dataset_id: str,
    ) -> bool:

        return dataset_id in cls._datasets

    @classmethod
    def remove(
        cls,
        dataset_id: str,
    ):

        cls._datasets.pop(dataset_id, None)

    @classmethod
    def list(cls):

        return list(cls._datasets.keys())

    @classmethod
    def all(cls):

        return cls._datasets