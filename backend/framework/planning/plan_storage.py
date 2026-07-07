from __future__ import annotations

from pathlib import Path

from backend.framework.planning.execution_plan import ExecutionPlan
from backend.framework.planning.plan_serializer import plan_serializer
from backend.framework.planning.plan_deserializer import plan_deserializer


class PlanStorage:

    def save(
        self,
        plan: ExecutionPlan,
        filepath: str | Path,
    ) -> None:

        filepath = Path(filepath)

        filepath.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        filepath.write_text(
            plan_serializer.to_json(plan),
            encoding="utf-8",
        )

    def load(
        self,
        filepath: str | Path,
    ) -> ExecutionPlan:

        filepath = Path(filepath)

        return plan_deserializer.from_json(
            filepath.read_text(
                encoding="utf-8",
            )
        )


plan_storage = PlanStorage()