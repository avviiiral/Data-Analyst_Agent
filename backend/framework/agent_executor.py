from __future__ import annotations

from backend.framework.registry import registry
from backend.framework.base_agent import AgentContext


class AgentExecutor:

    def execute(
        self,
        agent_name: str,
        dataset=None,
        memory=None,
        collaboration=None,
    ):

        agent = registry.create(agent_name)

        context = AgentContext(
            dataset=dataset,
            memory=memory or {},
            collaboration=collaboration,
        )

        return agent.run(context)

    def execute_many(
        self,
        agent_names: list[str],
        dataset=None,
        memory=None,
        collaboration=None,
    ):

        responses = []

        for name in agent_names:

            responses.append(
                self.execute(
                    agent_name=name,
                    dataset=dataset,
                    memory=memory,
                    collaboration=collaboration,
                )
            )

        return responses


executor = AgentExecutor()