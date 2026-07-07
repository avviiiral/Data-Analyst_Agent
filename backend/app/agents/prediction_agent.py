from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class PredictionAgent(BaseAgent):

    name = "PredictionAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Prediction completed.",
            data=None,
        )