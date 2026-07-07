from __future__ import annotations

from datetime import datetime


class TaskMetrics:

    def calculate(self, history):

        records = history.all()

        metrics = {
            "total_tasks": len(records),
            "completed": 0,
            "failed": 0,
            "running": 0,
            "pending": 0,
            "success_rate": 0.0,
            "generated_at": datetime.utcnow(),
        }

        for record in records:

            state = record["state"]

            if state == "COMPLETED":
                metrics["completed"] += 1

            elif state == "FAILED":
                metrics["failed"] += 1

            elif state == "RUNNING":
                metrics["running"] += 1

            elif state == "PENDING":
                metrics["pending"] += 1

        if metrics["total_tasks"]:

            metrics["success_rate"] = round(
                metrics["completed"] /
                metrics["total_tasks"] * 100,
                2,
            )

        return metrics


task_metrics = TaskMetrics()