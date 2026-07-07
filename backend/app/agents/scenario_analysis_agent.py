from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class ScenarioAnalysisAgent(BaseAgent):

    name = "ScenarioAnalysisAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Scenario analysis completed.",
            data=None,
        )