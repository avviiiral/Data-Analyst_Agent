from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class DuplicateAgent(BaseAgent):

    name = "DuplicateAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Duplicate analysis completed.",
            data=None,
        )