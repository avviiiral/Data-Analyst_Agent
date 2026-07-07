from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class PowerPointAgent(BaseAgent):

    name = "PowerPointAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="PowerPoint generated.",
            data=None,
        )