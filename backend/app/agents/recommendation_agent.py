from __future__ import annotations

from backend.analytics.recommendations import RecommendationEngine
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class RecommendationAgent(BaseAgent):

    name = "RecommendationAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:
        
        if context.dataset is None:
            raise ValueError("Dataset is required.")

        report = RecommendationEngine.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Recommendations generated.",
            data=report,
        )