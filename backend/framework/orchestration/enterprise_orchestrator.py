from __future__ import annotations

from backend.framework.planning.planning_engine import (
    planning_engine,
)

from backend.framework.orchestration.execution_engine import (
    execution_engine,
)

from backend.framework.orchestration.execution_monitor import (
    execution_monitor,
)


class EnterpriseOrchestrator:

    def run(
        self,
        query: str,
        dataset,
        memory=None,
    ) -> dict:

        execution_monitor.reset()

        plan, stages = planning_engine.create_plan(
            query,
        )

        summary = execution_engine.execute(
            stages=stages,
            dataset=dataset,
            memory=memory,
        )

        return {
            "plan": plan,
            "stages": stages,
            "summary": summary,
        }


enterprise_orchestrator = EnterpriseOrchestrator()