from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class RegressionAgent(BaseAgent):

    name = "RegressionAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Regression completed.",
            data=None,
        )