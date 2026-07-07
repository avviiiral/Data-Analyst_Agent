from __future__ import annotations

from backend.analytics.outliers import OutlierAnalyzer
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class OutlierAgent(BaseAgent):

    name = "OutlierAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = OutlierAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Outlier analysis completed.",
            data=report,
        )