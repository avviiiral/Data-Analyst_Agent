from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.file_validator import validate_file
from app.services.ai.chart_recommender import ChartRecommender
from app.services.ai.dataset_health import DatasetHealth
from app.services.ai.insight_generator import InsightGenerator
from app.services.ai.recommendation_engine import RecommendationEngine
from app.services.correlation_service import CorrelationService
from app.services.dataset_loader import DatasetLoader
from app.services.dataset_profiler import DatasetProfiler
from app.services.file_storage_service import FileStorageService
from app.services.missing_value_service import MissingValueService
from app.services.schema_detector import SchemaDetector
from app.services.statistics_service import StatisticsService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_file(
    file: UploadFile = File(...),
):
    validate_file(file)

    storage = FileStorageService()

    filename, path = storage.save(file)

    if not Path(path).exists():
        raise HTTPException(
            status_code=500,
            detail="Uploaded file was not saved.",
        )

    dataframe = DatasetLoader().load(path)

    profile = DatasetProfiler().profile(dataframe)

    schema = SchemaDetector().detect(dataframe)

    statistics = StatisticsService().summary(dataframe)

    correlation = CorrelationService().correlation(dataframe)

    missing_values = MissingValueService().analyze(dataframe)

    insights = InsightGenerator().generate(dataframe)

    recommendations = RecommendationEngine().recommend(dataframe)

    charts = ChartRecommender().recommend(dataframe)

    health_score = DatasetHealth().score(dataframe)

    return {
        "file": {
            "original_name": file.filename,
            "stored_name": filename,
            "path": path,
        },
        "profile": profile,
        "schema": schema,
        "statistics": statistics,
        "correlation": correlation,
        "missing_values": missing_values,
        "insights": insights,
        "recommendations": recommendations,
        "recommended_charts": charts,
        "dataset_health_score": health_score,
    }