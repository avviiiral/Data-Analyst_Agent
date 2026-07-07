from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class MonitoringAgent(BaseAgent):

    name = "MonitoringAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Monitoring completed.",
            data=None,
        )