from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class ForecastingAgent(BaseAgent):

    name = "ForecastingAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Forecasting completed.",
            data=None,
        )