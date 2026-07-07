from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class StorytellingAgent(BaseAgent):

    name = "StorytellingAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Storytelling completed.",
            data=None,
        )