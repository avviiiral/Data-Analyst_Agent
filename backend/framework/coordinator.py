from __future__ import annotations

from backend.framework.runtime import runtime
from backend.framework.agent_session import AgentSession


class AgentCoordinator:

    def execute(
        self,
        session: AgentSession,
    ):

        results = runtime.run(
            tasks=[task.name for task in session.plan],
            dataset=session.dataset,
            memory=session.metadata,
        )

        for item in results:

            session.add_result(
                item["agent"],
                item["response"],
            )

        return session


coordinator = AgentCoordinator()