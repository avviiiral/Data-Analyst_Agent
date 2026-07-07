from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class AutoMLAgent(BaseAgent):

    name = "AutoMLAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="AutoML completed.",
            data=None,
        )