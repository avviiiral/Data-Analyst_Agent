from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class AuditAgent(BaseAgent):

    name = "AuditAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Audit completed.",
            data=None,
        )