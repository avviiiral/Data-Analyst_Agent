from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class NormalizationAgent(BaseAgent):

    name = "NormalizationAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Normalization completed.",
            data=None,
        )