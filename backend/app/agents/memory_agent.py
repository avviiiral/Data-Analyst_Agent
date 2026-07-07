from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class MemoryAgent(BaseAgent):

    name = "MemoryAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Memory updated.",
            data=None,
        )