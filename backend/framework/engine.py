from __future__ import annotations

from backend.framework.agent_session import AgentSession
from backend.framework.coordinator import coordinator


class InsightForgeEngine:

    def execute(
        self,
        query: str,
        dataset,
        tasks: list[str],
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

        for task in tasks:

            session.add_task(task)

        return coordinator.execute(session)


engine = InsightForgeEngine()