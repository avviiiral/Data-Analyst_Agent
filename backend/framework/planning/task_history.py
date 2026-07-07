from __future__ import annotations

from datetime import datetime


class TaskHistory:

    def __init__(self):

        self._history = []

    def log(
        self,
        task,
    ):

        self._history.append(
            {
                "task": task.name,
                "agent": task.agent,
                "state": task.state.value,
                "timestamp": datetime.utcnow(),
            }
        )

    def all(self):

        return self._history

    def clear(self):

        self._history.clear()

    def count(self):

        return len(self._history)


task_history = TaskHistory()