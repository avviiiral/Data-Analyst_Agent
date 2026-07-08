from fastapi import APIRouter, HTTPException

from app.services.dataset_registry import DatasetRegistry
from app.services.schema_detector import SchemaDetector

router = APIRouter(
    prefix="/schema",
    tags=["Schema"],
)


@router.post("/")
def detect_schema(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "schema": SchemaDetector().detect(dataset.dataframe),
    }