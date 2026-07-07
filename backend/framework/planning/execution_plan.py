from __future__ import annotations

from dataclasses import dataclass, field

from backend.framework.planning.task import PlanningTask


@dataclass
class ExecutionPlan:

    query: str

    tasks: list[PlanningTask] = field(default_factory=list)

    estimated_steps: int = 0

    def add_task(
        self,
        task: PlanningTask,
    ):

        self.tasks.append(task)

        self.estimated_steps = len(self.tasks)

    def completed(self):

        return sum(
            task.completed
            for task in self.tasks
        )

    def pending(self):

        return self.estimated_steps - self.completed()

    def summary(self):

        return {
            "query": self.query,
            "tasks": self.estimated_steps,
            "completed": self.completed(),
            "pending": self.pending(),
        }