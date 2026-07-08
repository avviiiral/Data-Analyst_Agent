from fastapi import APIRouter, HTTPException

from app.services.dataset_registry import DatasetRegistry
from app.services.forecast_service import ForecastService

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
)


@router.post("/")
def forecast(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "forecast": ForecastService().forecast(dataset.dataframe),
    }