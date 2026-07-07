from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Self
from uuid import uuid4


class TaskStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass
class Task:

    name: str

    payload: dict[str, Any] = field(default_factory=dict)

    id: str = field(default_factory=lambda: str(uuid4()))

    status: TaskStatus = TaskStatus.PENDING

    assigned_agent: str | None = None
    
    dependencies: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)


    result: Any = None

    error: str | None = None
    
    def depends_on(
        self,
        *agents: str,
    ) -> Self:

        self.dependencies.extend(agents)
        return self