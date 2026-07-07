from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class ImbalanceAgent(BaseAgent):

    name = "ImbalanceAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Imbalance analysis completed.",
            data=None,
        )