from __future__ import annotations

from backend.analytics.distribution import DistributionAnalyzer
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class DistributionAgent(BaseAgent):

    name = "DistributionAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = DistributionAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Distribution analysis completed.",
            data=report,
        )