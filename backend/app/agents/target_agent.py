from __future__ import annotations

from backend.analytics.target_detector import TargetDetector
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class TargetAgent(BaseAgent):

    name = "TargetAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:
        
        if context.dataset is None:
            raise ValueError("Dataset is required.")

        report = TargetDetector.analyze(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Target detection completed.",
            data=report,
        )