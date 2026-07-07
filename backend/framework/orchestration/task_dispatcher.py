from __future__ import annotations

from backend.framework.orchestration.execution_queue import ExecutionQueue
from backend.framework.orchestration.worker_pool import WorkerPool


class TaskDispatcher:

    def dispatch(
        self,
        queue: ExecutionQueue,
        workers: WorkerPool,
    ):

        assignments = []

        while not queue.empty():

            worker = workers.available()

            if worker is None:
                break

            task = queue.dequeue()

            worker.assign(task.agent)

            assignments.append(
                (
                    worker,
                    task,
                )
            )

        return assignments


task_dispatcher = TaskDispatcher()