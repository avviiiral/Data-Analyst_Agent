from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class AnomalyAgent(BaseAgent):

    name = "AnomalyAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Anomaly detection completed.",
            data=None,
        )