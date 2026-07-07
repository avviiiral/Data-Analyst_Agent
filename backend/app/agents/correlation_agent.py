from __future__ import annotations

from backend.analytics.correlation import CorrelationAnalyzer
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class CorrelationAgent(BaseAgent):

    name = "CorrelationAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = CorrelationAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Correlation analysis completed.",
            data=report,
        )