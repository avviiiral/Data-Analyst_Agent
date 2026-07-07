from __future__ import annotations

from backend.framework.agent_router import router


class AgentSelector:

    def select(
        self,
        tasks: list[str],
    ) -> dict[str, str]:

        selected = {}

        for task in tasks:

            selected[task] = router.route(task)

        return selected


selector = AgentSelector()