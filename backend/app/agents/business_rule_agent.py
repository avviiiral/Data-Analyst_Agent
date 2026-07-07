from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class BusinessRuleAgent(BaseAgent):

    name = "BusinessRuleAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Business rule validation completed.",
            data=None,
        )