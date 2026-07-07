from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)
from backend.analytics.statistics import StatisticsAnalyzer


class StatisticsAgent(BaseAgent):

    name = "StatisticsAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = StatisticsAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Statistics generated.",
            data=report,
        )