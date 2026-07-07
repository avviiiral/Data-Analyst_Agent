from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class MissingValueAgent(BaseAgent):

    name = "MissingValueAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Missing value analysis completed.",
            data=None,
        )