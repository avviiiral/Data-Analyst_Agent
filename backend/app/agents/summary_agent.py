from __future__ import annotations

from backend.analytics.summary import ExecutiveSummaryGenerator
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class SummaryAgent(BaseAgent):

    name = "SummaryAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = ExecutiveSummaryGenerator.generate(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Executive summary generated.",
            data=report,
        )