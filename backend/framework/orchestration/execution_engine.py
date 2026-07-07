from __future__ import annotations

from backend.framework.orchestration.execution_queue import ExecutionQueue
from backend.framework.orchestration.worker_pool import WorkerPool
from backend.framework.orchestration.task_dispatcher import (
    task_dispatcher,
)
from backend.framework.orchestration.parallel_executor import (
    parallel_executor,
)
from backend.framework.orchestration.result_aggregator import (
    result_aggregator,
)


class ExecutionEngine:

    def execute(
        self,
        stages=None,
        dataset=None,
        memory=None,
        workers: int = 4,
        tasks=None,
    ):
        # Backward compatibility
        if tasks is not None:
            stages = [tasks]

        if stages is None:
            raise ValueError("Either 'stages' or 'tasks' must be provided.")

        all_responses = []

        for stage in stages:

            queue = ExecutionQueue()

            for task in stage:

                queue.enqueue(task)

            worker_pool = WorkerPool(workers)

            while not queue.empty():

                assignments = task_dispatcher.dispatch(
                    queue,
                    worker_pool,
                )

                if not assignments:
                    break

                responses = parallel_executor.execute(
                    assignments,
                    dataset=dataset,
                    memory=memory,
                )

                all_responses.extend(
                    responses,
                )

                for worker, _ in assignments:

                    worker.release()

        return result_aggregator.aggregate(
            all_responses,
        )


execution_engine = ExecutionEngine()