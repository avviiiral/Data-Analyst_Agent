from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

from backend.framework.agent_executor import executor


class ParallelExecutor:

    def execute(
        self,
        assignments,
        dataset,
        memory=None,
        collaboration=None,
    ):

        results = []

        with ThreadPoolExecutor(
            max_workers=len(assignments),
        ) as pool:

            futures = []

            for worker, task in assignments:

                futures.append(
                    pool.submit(
                        executor.execute,
                        agent_name=task.agent,
                        dataset=dataset,
                        memory=memory,
                        collaboration=collaboration,
                    )
                )

            for future in as_completed(futures):

                results.append(
                    future.result()
                )

        return results


parallel_executor = ParallelExecutor()