from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)
from backend.preprocessing.schema_detector import SchemaDetector


class SchemaAgent(BaseAgent):

    name = "SchemaAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        report = SchemaDetector.detect(
            context.dataset.dataframe
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Schema detection completed.",
            data=report,
        )