from __future__ import annotations

from datetime import datetime


class ExecutionMonitor:

    def __init__(self):

        self.reset()

    def reset(self):

        self._records = []

    def start(
        self,
        task: str,
    ):

        self._records.append(
            {
                "task": task,
                "status": "RUNNING",
                "started": datetime.now(),
                "finished": None,
            }
        )

    def finish(
        self,
        task: str,
    ):

        for record in reversed(self._records):

            if (
                record["task"] == task
                and record["status"] == "RUNNING"
            ):

                record["status"] = "COMPLETED"
                record["finished"] = datetime.now()
                break

    def fail(
        self,
        task: str,
    ):

        for record in reversed(self._records):

            if (
                record["task"] == task
                and record["status"] == "RUNNING"
            ):

                record["status"] = "FAILED"
                record["finished"] = datetime.now()
                break

    def records(self):

        return self._records

    def summary(self):

        completed = sum(
            r["status"] == "COMPLETED"
            for r in self._records
        )

        failed = sum(
            r["status"] == "FAILED"
            for r in self._records
        )

        running = sum(
            r["status"] == "RUNNING"
            for r in self._records
        )

        return {
            "total": len(self._records),
            "completed": completed,
            "failed": failed,
            "running": running,
        }


execution_monitor = ExecutionMonitor()