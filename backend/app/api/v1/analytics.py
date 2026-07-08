from fastapi import APIRouter, HTTPException

from app.services.ai.insight_generator import InsightGenerator
from app.services.ai.recommendation_engine import RecommendationEngine
from app.services.correlation_service import CorrelationService
from app.services.dataset_registry import DatasetRegistry
from app.services.missing_value_service import MissingValueService
from app.services.statistics_service import StatisticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.post("/")
def analytics(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "statistics": StatisticsService().summary(dataset.dataframe),
        "missing_values": MissingValueService().analyze(dataset.dataframe),
        "correlation": CorrelationService().correlation(dataset.dataframe),
        "insights": InsightGenerator().generate(dataset.dataframe),
        "recommendations": RecommendationEngine().recommend(dataset.dataframe),
    }