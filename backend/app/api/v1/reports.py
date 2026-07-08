from fastapi import APIRouter, HTTPException

from app.services.dataset_registry import DatasetRegistry
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.post("/")
def report(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "report": ReportService().generate(dataset.dataframe),
    }