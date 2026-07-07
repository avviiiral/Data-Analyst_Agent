from __future__ import annotations

from backend.analytics.profiler import DataProfiler
from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class ProfilerAgent(BaseAgent):

    name = "ProfilerAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = DataProfiler.profile(
            context.dataset
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Dataset profiling completed.",
            data=report,
        )