from fastapi import APIRouter, HTTPException

from app.services.ai.chart_recommender import ChartRecommender
from app.services.ai.dataset_health import DatasetHealth
from app.services.ai.insight_generator import InsightGenerator
from app.services.ai.recommendation_engine import RecommendationEngine
from app.services.correlation_service import CorrelationService
from app.services.dataset_profiler import DatasetProfiler
from app.services.dataset_registry import DatasetRegistry
from app.services.missing_value_service import MissingValueService
from app.services.schema_detector import SchemaDetector
from app.services.statistics_service import StatisticsService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.post("/")
def dashboard(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "profile": DatasetProfiler().profile(dataset.dataframe),
        "schema": SchemaDetector().detect(dataset.dataframe),
        "statistics": StatisticsService().summary(dataset.dataframe),
        "correlation": CorrelationService().correlation(dataset.dataframe),
        "missing_values": MissingValueService().analyze(dataset.dataframe),
        "insights": InsightGenerator().generate(dataset.dataframe),
        "recommendations": RecommendationEngine().recommend(dataset.dataframe),
        "recommended_charts": ChartRecommender().recommend(dataset.dataframe),
        "dataset_health_score": DatasetHealth().score(dataset.dataframe),
    }