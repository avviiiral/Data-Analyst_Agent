from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)
from backend.visualization.chart_selector import ChartSelector


class VisualizationAgent(BaseAgent):

    name = "VisualizationAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        chart = ChartSelector.recommend(
            context.dataset.dataframe
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Visualization generated.",
            data=chart,
        )