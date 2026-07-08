from fastapi import APIRouter, HTTPException

from app.services.correlation_service import CorrelationService
from app.services.dataset_profiler import DatasetProfiler
from app.services.dataset_registry import DatasetRegistry
from app.services.missing_value_service import MissingValueService
from app.services.outlier_service import OutlierService
from app.services.statistics_service import StatisticsService

router = APIRouter(
    prefix="/profiler",
    tags=["Profiler"],
)


@router.post("/")
def profile_dataset(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "profile": DatasetProfiler().profile(dataset.dataframe),
        "statistics": StatisticsService().summary(dataset.dataframe),
        "missing_values": MissingValueService().analyze(dataset.dataframe),
        "correlation": CorrelationService().correlation(dataset.dataframe),
        "outliers": OutlierService().detect(dataset.dataframe),
    }