from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class ExportAgent(BaseAgent):

    name = "ExportAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Export completed.",
            data=None,
        )