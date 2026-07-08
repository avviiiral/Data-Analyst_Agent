from __future__ import annotations

from backend.framework.agent_selector import selector
from backend.framework.agent_executor import executor


class Workflow:

    def run(
        self,
        tasks,
        dataset=None,
        memory=None,
    ):

        responses = []

        for task in tasks:

            task_name = task.name if hasattr(task, "name") else task

            agent = selector.select([task_name])[task_name]

            response = executor.execute(
                agent_name=agent,
                dataset=dataset,
                memory=memory,
            )

            responses.append(
                {
                    "task": task_name,
                    "agent": agent,
                    "response": response,
                }
            )

        return responses


workflow = Workflow()