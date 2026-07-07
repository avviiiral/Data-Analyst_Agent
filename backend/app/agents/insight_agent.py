from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)
from backend.analytics.insights import InsightAnalyzer


class InsightAgent(BaseAgent):

    name = "InsightAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = InsightAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Insights generated.",
            data=report,
        )