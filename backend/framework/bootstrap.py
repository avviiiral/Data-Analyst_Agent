from backend.framework.registry import registry

from backend.agents.schema_agent import SchemaAgent
from backend.agents.data_agent import DataAgent
from backend.agents.profiler_agent import ProfilerAgent
from backend.agents.statistics_agent import StatisticsAgent
from backend.agents.correlation_agent import CorrelationAgent
from backend.agents.distribution_agent import DistributionAgent
from backend.agents.health_agent import HealthAgent
from backend.agents.quality_agent import QualityAgent
from backend.agents.outlier_agent import OutlierAgent
from backend.agents.target_agent import TargetAgent
from backend.agents.recommendation_agent import RecommendationAgent
from backend.agents.summary_agent import SummaryAgent
from backend.agents.kpi_agent import KPIAgent
from backend.agents.query_agent import QueryAgent
from backend.agents.visualization_agent import VisualizationAgent
from backend.agents.insight_agent import InsightAgent

from backend.agents.forecast_agent import ForecastAgent
from backend.agents.trend_agent import TrendAgent
from backend.agents.timeseries_agent import TimeSeriesAgent
from backend.agents.seasonality_agent import SeasonalityAgent
from backend.agents.anomaly_agent import AnomalyAgent

from backend.agents.cleaning_agent import CleaningAgent
from backend.agents.missing_value_agent import MissingValueAgent
from backend.agents.encoding_agent import EncodingAgent
from backend.agents.feature_engineering_agent import FeatureEngineeringAgent
from backend.agents.transformation_agent import TransformationAgent

from backend.agents.automl_agent import AutoMLAgent
from backend.agents.classification_agent import ClassificationAgent
from backend.agents.regression_agent import RegressionAgent
from backend.agents.clustering_agent import ClusteringAgent
from backend.agents.forecasting_agent import ForecastingAgent
from backend.agents.prediction_agent import PredictionAgent
from backend.agents.feature_selection_agent import FeatureSelectionAgent
from backend.agents.model_evaluation_agent import ModelEvaluationAgent
from backend.agents.explainability_agent import ExplainabilityAgent

from backend.agents.dashboard_agent import DashboardAgent
from backend.agents.report_agent import ReportAgent
from backend.agents.powerpoint_agent import PowerPointAgent
from backend.agents.export_agent import ExportAgent
from backend.agents.storytelling_agent import StorytellingAgent

from backend.agents.sql_agent import SQLAgent
from backend.agents.python_agent import PythonAgent
from backend.agents.prompt_agent import PromptAgent
from backend.agents.workflow_agent import WorkflowAgent

from backend.agents.data_validation_agent import DataValidationAgent
from backend.agents.duplicate_agent import DuplicateAgent
from backend.agents.normalization_agent import NormalizationAgent
from backend.agents.scaling_agent import ScalingAgent
from backend.agents.sampling_agent import SamplingAgent
from backend.agents.imbalance_agent import ImbalanceAgent

from backend.agents.business_rule_agent import BusinessRuleAgent
from backend.agents.root_cause_agent import RootCauseAgent
from backend.agents.diagnostic_agent import DiagnosticAgent
from backend.agents.driver_analysis_agent import DriverAnalysisAgent
from backend.agents.scenario_analysis_agent import ScenarioAnalysisAgent
from backend.agents.whatif_agent import WhatIfAgent

from backend.agents.chat_agent import ChatAgent
from backend.agents.memory_agent import MemoryAgent
from backend.agents.planning_agent import PlanningAgent
from backend.agents.execution_agent import ExecutionAgent
from backend.agents.monitoring_agent import MonitoringAgent
from backend.agents.audit_agent import AuditAgent
from backend.agents.security_agent import SecurityAgent

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