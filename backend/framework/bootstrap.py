from backend.framework.registry import registry

from backend.app.agents.schema_agent import SchemaAgent
from backend.app.agents.data_agent import DataAgent
from backend.app.agents.profiler_agent import ProfilerAgent
from backend.app.agents.statistics_agent import StatisticsAgent
from backend.app.agents.correlation_agent import CorrelationAgent
from backend.app.agents.distribution_agent import DistributionAgent
from backend.app.agents.health_agent import HealthAgent
from backend.app.agents.quality_agent import QualityAgent
from backend.app.agents.outlier_agent import OutlierAgent
from backend.app.agents.target_agent import TargetAgent
from backend.app.agents.recommendation_agent import RecommendationAgent
from backend.app.agents.summary_agent import SummaryAgent
from backend.app.agents.kpi_agent import KPIAgent
from backend.app.agents.query_agent import QueryAgent
from backend.app.agents.visualization_agent import VisualizationAgent
from backend.app.agents.insight_agent import InsightAgent

from backend.app.agents.forecast_agent import ForecastAgent
from backend.app.agents.trend_agent import TrendAgent
from backend.app.agents.timeseries_agent import TimeSeriesAgent
from backend.app.agents.seasonality_agent import SeasonalityAgent
from backend.app.agents.anomaly_agent import AnomalyAgent

from backend.app.agents.cleaning_agent import CleaningAgent
from backend.app.agents.missing_value_agent import MissingValueAgent
from backend.app.agents.encoding_agent import EncodingAgent
from backend.app.agents.feature_engineering_agent import FeatureEngineeringAgent
from backend.app.agents.transformation_agent import TransformationAgent

from backend.app.agents.automl_agent import AutoMLAgent
from backend.app.agents.classification_agent import ClassificationAgent
from backend.app.agents.regression_agent import RegressionAgent
from backend.app.agents.clustering_agent import ClusteringAgent
from backend.app.agents.forecasting_agent import ForecastingAgent
from backend.app.agents.prediction_agent import PredictionAgent
from backend.app.agents.feature_selection_agent import FeatureSelectionAgent
from backend.app.agents.model_evaluation_agent import ModelEvaluationAgent
from backend.app.agents.explainability_agent import ExplainabilityAgent

from backend.app.agents.dashboard_agent import DashboardAgent
from backend.app.agents.report_agent import ReportAgent
from backend.app.agents.powerpoint_agent import PowerPointAgent
from backend.app.agents.export_agent import ExportAgent
from backend.app.agents.storytelling_agent import StorytellingAgent

from backend.app.agents.sql_agent import SQLAgent
from backend.app.agents.python_agent import PythonAgent
from backend.app.agents.prompt_agent import PromptAgent
from backend.app.agents.workflow_agent import WorkflowAgent

from backend.app.agents.data_validation_agent import DataValidationAgent
from backend.app.agents.duplicate_agent import DuplicateAgent
from backend.app.agents.normalization_agent import NormalizationAgent
from backend.app.agents.scaling_agent import ScalingAgent
from backend.app.agents.sampling_agent import SamplingAgent
from backend.app.agents.imbalance_agent import ImbalanceAgent

from backend.app.agents.business_rule_agent import BusinessRuleAgent
from backend.app.agents.root_cause_agent import RootCauseAgent
from backend.app.agents.diagnostic_agent import DiagnosticAgent
from backend.app.agents.driver_analysis_agent import DriverAnalysisAgent
from backend.app.agents.scenario_analysis_agent import ScenarioAnalysisAgent
from backend.app.agents.whatif_agent import WhatIfAgent

from backend.app.agents.chat_agent import ChatAgent
from backend.app.agents.memory_agent import MemoryAgent
from backend.app.agents.planning_agent import PlanningAgent
from backend.app.agents.execution_agent import ExecutionAgent
from backend.app.agents.monitoring_agent import MonitoringAgent
from backend.app.agents.audit_agent import AuditAgent
from backend.app.agents.security_agent import SecurityAgent

def bootstrap() -> None:

    registry.clear()

    registry.register(SchemaAgent)
    registry.register(DataAgent)
    registry.register(ProfilerAgent)
    registry.register(StatisticsAgent)
    registry.register(CorrelationAgent)
    registry.register(DistributionAgent)
    registry.register(HealthAgent)
    registry.register(QualityAgent)
    registry.register(OutlierAgent)
    registry.register(TargetAgent)
    registry.register(RecommendationAgent)
    registry.register(SummaryAgent)
    registry.register(KPIAgent)
    registry.register(QueryAgent)
    registry.register(VisualizationAgent)
    registry.register(InsightAgent)

    registry.register(ForecastAgent)
    registry.register(TrendAgent)
    registry.register(TimeSeriesAgent)
    registry.register(SeasonalityAgent)
    registry.register(AnomalyAgent)
    registry.register(CleaningAgent)
    registry.register(MissingValueAgent)
    registry.register(EncodingAgent)
    registry.register(FeatureEngineeringAgent)
    registry.register(TransformationAgent)
    
    registry.register(AutoMLAgent)
    registry.register(ClassificationAgent)
    registry.register(RegressionAgent)
    registry.register(ClusteringAgent)
    registry.register(ForecastingAgent)
    registry.register(PredictionAgent)
    registry.register(FeatureSelectionAgent)
    registry.register(ModelEvaluationAgent)
    registry.register(ExplainabilityAgent)

    registry.register(DashboardAgent)
    registry.register(ReportAgent)
    registry.register(PowerPointAgent)
    registry.register(ExportAgent)
    registry.register(StorytellingAgent)

    registry.register(SQLAgent)
    registry.register(PythonAgent)
    registry.register(PromptAgent)
    registry.register(WorkflowAgent)

    registry.register(DataValidationAgent)
    registry.register(DuplicateAgent)
    registry.register(NormalizationAgent)
    registry.register(ScalingAgent)
    registry.register(SamplingAgent)
    registry.register(ImbalanceAgent)

    registry.register(BusinessRuleAgent)
    registry.register(RootCauseAgent)
    registry.register(DiagnosticAgent)
    registry.register(DriverAnalysisAgent)
    registry.register(ScenarioAnalysisAgent)
    registry.register(WhatIfAgent)

    registry.register(ChatAgent)
    registry.register(MemoryAgent)
    registry.register(PlanningAgent)
    registry.register(ExecutionAgent)
    registry.register(MonitoringAgent)
    registry.register(AuditAgent)
    registry.register(SecurityAgent)