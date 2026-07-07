from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)
from backend.analytics.profiler import DataProfiler


class DataAgent(BaseAgent):

    name = "DataAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        dataset = context.dataset

        profile = DataProfiler.profile(dataset)

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Dataset profiling completed.",
            data=profile,
        )