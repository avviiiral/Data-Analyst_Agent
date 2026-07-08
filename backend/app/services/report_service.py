import pandas as pd

from app.services.ai.dataset_health import DatasetHealth
from app.services.ai.insight_generator import InsightGenerator
from app.services.ai.recommendation_engine import RecommendationEngine
from app.services.correlation_service import CorrelationService
from app.services.dataset_profiler import DatasetProfiler
from app.services.missing_value_service import MissingValueService
from app.services.schema_detector import SchemaDetector
from app.services.statistics_service import StatisticsService


class ReportService:

    def generate(
        self,
        dataframe: pd.DataFrame,
    ):

        return {
            "executive_summary": {
                "rows": int(len(dataframe)),
                "columns": int(len(dataframe.columns)),
                "health_score": DatasetHealth().score(dataframe),
            },
            "profile": DatasetProfiler().profile(dataframe),
            "schema": SchemaDetector().detect(dataframe),
            "statistics": StatisticsService().summary(dataframe),
            "missing_values": MissingValueService().analyze(dataframe),
            "correlation": CorrelationService().correlation(dataframe),
            "insights": InsightGenerator().generate(dataframe),
            "recommendations": RecommendationEngine().recommend(dataframe),
        }