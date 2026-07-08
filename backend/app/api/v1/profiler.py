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

    dataframe = DatasetRegistry.get(dataset_id)

    if dataframe is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "profile": DatasetProfiler().profile(dataframe),
        "statistics": StatisticsService().summary(dataframe),
        "missing_values": MissingValueService().analyze(dataframe),
        "correlation": CorrelationService().correlation(dataframe),
        "outliers": OutlierService().detect(dataframe),
    }