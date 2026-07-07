from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class DataValidationAgent(BaseAgent):

    name = "DataValidationAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Data validation completed.",
            data=None,
        )