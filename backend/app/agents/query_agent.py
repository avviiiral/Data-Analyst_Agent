from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
    BaseAgent,
)


class QueryAgent(BaseAgent):

    name = "QueryAgent"

    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:

        query = context.memory.get("query", "")

        return AgentResponse(
            success=True,
            agent=self.name,
            message="Natural language query received.",
            data={
                "query": query,
            },
        )