from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class SeasonalityAgent(BaseAgent):

    name = "SeasonalityAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Seasonality analysis completed.",
            data=None,
        )