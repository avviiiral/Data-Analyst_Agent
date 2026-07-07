from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ExecutionRecord:
    timestamp: datetime
    agent: str
    success: bool
    message: str
    data: Any = None


class ExecutionHistory:

    def __init__(self):
        self._history: list[ExecutionRecord] = []

    def add(self, record: ExecutionRecord):
        self._history.append(record)

    def all(self):
        return list(self._history)

    def clear(self):
        self._history.clear()

    def count(self):
        return len(self._history)


execution_history = ExecutionHistory()