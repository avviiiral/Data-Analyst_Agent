from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class SQLAgent(BaseAgent):

    name = "SQLAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="SQL processing completed.",
            data=None,
        )