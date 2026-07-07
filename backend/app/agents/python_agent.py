from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class PythonAgent(BaseAgent):

    name = "PythonAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Python execution completed.",
            data=None,
        )