from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)
from app.services.schema_detector import SchemaDetector


class SchemaAgent(BaseAgent):

    name = "SchemaAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:
        
        if context.dataset is None:
            raise ValueError("Dataset is required.")

        report = SchemaDetector().detect(
            context.dataset.dataframe
        )

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Schema detection completed.",
            data=report,
        )