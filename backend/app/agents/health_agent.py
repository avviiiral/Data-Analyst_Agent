from __future__ import annotations

from backend.analytics.health import DatasetHealthAnalyzer
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class HealthAgent(BaseAgent):

    name = "HealthAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = DatasetHealthAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Dataset health analysis completed.",
            data=report,
        )