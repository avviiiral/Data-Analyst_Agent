from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class ModelEvaluationAgent(BaseAgent):

    name = "ModelEvaluationAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Model evaluation completed.",
            data=None,
        )