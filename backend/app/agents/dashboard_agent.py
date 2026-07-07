from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class DashboardAgent(BaseAgent):

    name = "DashboardAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Dashboard generated.",
            data=None,
        )