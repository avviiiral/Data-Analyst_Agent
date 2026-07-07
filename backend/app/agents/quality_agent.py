from __future__ import annotations

from backend.analytics.quality import DataQualityAnalyzer
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class QualityAgent(BaseAgent):

    name = "QualityAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = DataQualityAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Data quality analysis completed.",
            data=report,
        )