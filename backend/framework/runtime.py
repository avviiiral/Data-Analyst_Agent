from __future__ import annotations

from backend.framework.workflow import workflow


class AgentRuntime:

    def run(
        self,
        tasks: list[str],
        dataset=None,
        memory=None,
    ):

        return workflow.run(
            tasks=tasks,
            dataset=dataset,
            memory=memory,
        )

    def run_task(
        self,
        task: str,
        dataset=None,
        memory=None,
    ):

        result = workflow.run(
            tasks=[task],
            dataset=dataset,
            memory=memory,
        )

        return result[0]


runtime = AgentRuntime()