from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd


@dataclass
class Dataset:

    id: str | None = None

    name: str = ""

    path: str = ""

    dataframe: pd.DataFrame = field(
        default_factory=pd.DataFrame,
    )

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    @property
    def rows(self) -> int:

        return len(self.dataframe)

    @property
    def columns(self) -> int:

        return len(self.dataframe.columns)

    @property
    def column_names(self) -> list[str]:

        return self.dataframe.columns.tolist()

    @property
    def numeric_columns(self) -> list[str]:

        return self.dataframe.select_dtypes(
            include="number",
        ).columns.tolist()

    @property
    def categorical_columns(self) -> list[str]:

        return self.dataframe.select_dtypes(
            exclude="number",
        ).columns.tolist()

    @property
    def shape(self):

        return self.dataframe.shape

    @classmethod
    def from_dataframe(
        cls,
        dataframe: pd.DataFrame,
        name: str = "",
        path: str = "",
        dataset_id: str | None = None,
    ):

        if not name and path:
            name = Path(path).stem

        return cls(
            id=dataset_id,
            name=name,
            path=path,
            dataframe=dataframe,
        )

    def copy(self):

        return Dataset(
            id=self.id,
            name=self.name,
            path=self.path,
            dataframe=self.dataframe.copy(),
            metadata=self.metadata.copy(),
        )