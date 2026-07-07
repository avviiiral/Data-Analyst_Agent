from __future__ import annotations

from enum import Enum


class TaskState(str, Enum):

    PENDING = "PENDING"

    READY = "READY"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    SKIPPED = "SKIPPED"