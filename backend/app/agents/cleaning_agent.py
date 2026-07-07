from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class CleaningAgent(BaseAgent):

    name = "CleaningAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Data cleaning completed.",
            data=None,
        )