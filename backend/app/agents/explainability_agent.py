from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class ExplainabilityAgent(BaseAgent):

    name = "ExplainabilityAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Explainability completed.",
            data=None,
        )