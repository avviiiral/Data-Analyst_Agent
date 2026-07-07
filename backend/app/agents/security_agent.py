from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class SecurityAgent(BaseAgent):

    name = "SecurityAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Security checks completed.",
            data=None,
        )