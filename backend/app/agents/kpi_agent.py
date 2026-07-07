from __future__ import annotations

from backend.analytics.business_kpi import BusinessKPIAnalyzer
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class KPIAgent(BaseAgent):

    name = "KPIAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = BusinessKPIAnalyzer.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Business KPIs generated.",
            data=report,
        )