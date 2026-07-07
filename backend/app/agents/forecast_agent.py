from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class ForecastAgent(BaseAgent):

    name = "ForecastAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Forecast analysis completed.",
            data=None,
        )