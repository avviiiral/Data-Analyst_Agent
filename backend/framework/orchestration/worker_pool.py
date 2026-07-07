from __future__ import annotations

from backend.framework.orchestration.worker import Worker


class WorkerPool:

    def __init__(
        self,
        workers: int = 4,
    ):

        self._workers = [
            Worker(i + 1)
            for i in range(workers)
        ]

    def available(self) -> Worker | None:

        idle = self.idle()

        if not idle:
            return None

        return sorted(
            idle,
            key=lambda worker: worker.id,
        )[0]

    def all(self) -> list[Worker]:

        return self._workers

    def busy(self) -> list[Worker]:

        return [
            worker
            for worker in self._workers
            if worker.busy
        ]

    def idle(self) -> list[Worker]:

        return [
            worker
            for worker in self._workers
            if not worker.busy
        ]

    def count(self) -> int:

        return len(self._workers)