from __future__ import annotations

from collections import deque

from backend.framework.planning.task import PlanningTask


class ExecutionQueue:

    def __init__(self):

        self._queue = deque()

    def enqueue(
        self,
        task: PlanningTask,
    ) -> None:

        self._queue.append(task)

    def dequeue(self) -> PlanningTask | None:

        if self.empty():
            return None

        return self._queue.popleft()

    def peek(self) -> PlanningTask | None:

        if self.empty():
            return None

        return self._queue[0]

    def empty(self) -> bool:

        return len(self._queue) == 0

    def size(self) -> int:

        return len(self._queue)

    def clear(self) -> None:

        self._queue.clear()

    def all(self):

        return list(self._queue)


execution_queue = ExecutionQueue()