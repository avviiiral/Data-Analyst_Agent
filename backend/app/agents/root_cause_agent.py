from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class RootCauseAgent(BaseAgent):

    name = "RootCauseAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Root cause analysis completed.",
            data=None,
        )