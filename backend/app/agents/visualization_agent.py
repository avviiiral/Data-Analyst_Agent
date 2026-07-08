from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)
from app.services.ai.chart_recommender import ChartRecommender


class VisualizationAgent(BaseAgent):

    name = "VisualizationAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:
        
        if context.dataset is None:
            raise ValueError("Dataset is required.")

        chart = ChartRecommender().recommend(
            context.dataset.dataframe
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Visualization generated.",
            data=chart,
        )