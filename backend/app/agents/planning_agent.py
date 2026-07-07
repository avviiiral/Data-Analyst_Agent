from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class PlanningAgent(BaseAgent):

    name = "PlanningAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Planning completed.",
            data=None,
        )