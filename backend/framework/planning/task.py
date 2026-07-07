from __future__ import annotations

from dataclasses import dataclass, field

from backend.framework.planning.task_state import TaskState


@dataclass
class PlanningTask:

    name: str

    priority: int = 5

    dependencies: list[str] = field(default_factory=list)

    agent: str | None = None

    completed: bool = False

    state: TaskState = TaskState.PENDING