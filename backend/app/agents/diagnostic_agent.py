from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class DiagnosticAgent(BaseAgent):

    name = "DiagnosticAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Diagnostic analysis completed.",
            data=None,
        )