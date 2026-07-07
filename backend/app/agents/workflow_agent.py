from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class WorkflowAgent(BaseAgent):

    name = "WorkflowAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Workflow execution completed.",
            data=None,
        )