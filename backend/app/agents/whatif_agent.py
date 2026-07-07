from __future__ import annotations

from backend.framework.base_agent import AgentContext, AgentResponse, BaseAgent


class WhatIfAgent(BaseAgent):

    name = "WhatIfAgent"

    def run(self, context: AgentContext) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="What-if analysis completed.",
            data=None,
        )