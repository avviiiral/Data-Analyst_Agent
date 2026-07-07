from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class PromptAgent(BaseAgent):

    name = "PromptAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Prompt processing completed.",
            data=None,
        )