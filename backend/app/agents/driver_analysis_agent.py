from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class DriverAnalysisAgent(BaseAgent):

    name = "DriverAnalysisAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Driver analysis completed.",
            data=None,
        )