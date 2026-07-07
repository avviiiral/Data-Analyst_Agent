from __future__ import annotations

from backend.framework.registry import registry


class AgentRouter:

    def route(self, task_name: str):

        mapping = {
            "schema": "SchemaAgent",
            "profile": "ProfilerAgent",
            "statistics": "StatisticsAgent",
            "correlation": "CorrelationAgent",
            "distribution": "DistributionAgent",
            "outlier": "OutlierAgent",
            "quality": "QualityAgent",
            "health": "HealthAgent",
            "recommendation": "RecommendationAgent",
            "summary": "SummaryAgent",
            "kpi": "KPIAgent",
            "insight": "InsightAgent",
            "visualization": "VisualizationAgent",
            "forecast": "ForecastAgent",
            "forecasting": "ForecastingAgent",
            "trend": "TrendAgent",
            "timeseries": "TimeSeriesAgent",
            "seasonality": "SeasonalityAgent",
            "anomaly": "AnomalyAgent",
            "target": "TargetAgent",
            "clean": "CleaningAgent",
            "missing": "MissingValueAgent",
            "encoding": "EncodingAgent",
            "feature": "FeatureEngineeringAgent",
            "transform": "TransformationAgent",
            "sql": "SQLAgent",
            "python": "PythonAgent",
            "dashboard": "DashboardAgent",
            "report": "ReportAgent",
            "powerpoint": "PowerPointAgent",
            "export": "ExportAgent",
            "story": "StorytellingAgent",
            "classification": "ClassificationAgent",
            "regression": "RegressionAgent",
            "clustering": "ClusteringAgent",
            "prediction": "PredictionAgent",
            "automl": "AutoMLAgent",
        }

        task = task_name.lower()

        for keyword, agent in mapping.items():

            if keyword in task and agent in registry.names():

                return agent

        return "DataAgent"


router = AgentRouter()