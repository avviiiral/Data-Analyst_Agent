from __future__ import annotations

from backend.framework.agent_selector import selector
from backend.framework.agent_executor import executor


class Workflow:

    def run(
        self,
        tasks: list[str],
        dataset=None,
        memory=None,
    ):

        mapping = selector.select(tasks)

        responses = []

        for task, agent in mapping.items():

            response = executor.execute(
                agent_name=agent,
                dataset=dataset,
                memory=memory,
            )

            responses.append(
                {
                    "task": task,
                    "agent": agent,
                    "response": response,
                }
            )

        return responses


workflow = Workflow()