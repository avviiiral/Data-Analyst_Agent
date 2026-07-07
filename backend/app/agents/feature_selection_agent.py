from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class FeatureSelectionAgent(BaseAgent):

    name = "FeatureSelectionAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Feature selection completed.",
            data=None,
        )