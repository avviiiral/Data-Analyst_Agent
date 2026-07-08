from __future__ import annotations

from backend.framework.agent_session import AgentSession
from backend.framework.coordinator import coordinator
from backend.framework.planning.planning_engine import planning_engine


class InsightForgeEngine:

    def execute(
        self,
        query: str,
        dataset=None,
        metadata: dict | None = None,
    ):

        session = AgentSession()

        session.set_query(query)

        session.set_dataset(dataset)

        if metadata:

            for key, value in metadata.items():

                session.set_metadata(
                    key,
                    value,
                )

        plan, _ = planning_engine.create_plan(query)

        for task in plan.tasks:

            session.add_task(task)

        return coordinator.execute(session)


engine = InsightForgeEngine()