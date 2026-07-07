from __future__ import annotations

from backend.framework.planning.task_state import TaskState
from backend.framework.planning.execution_plan import ExecutionPlan


class TaskTracker:

    def initialize(
        self,
        plan: ExecutionPlan,
    ):

        for task in plan.tasks:

            task.state = TaskState.PENDING

        return plan

    def start(self, task):

        task.state = TaskState.RUNNING

    def complete(self, task):

        task.state = TaskState.COMPLETED

        task.completed = True

    def fail(self, task):

        task.state = TaskState.FAILED

        task.completed = False


tracker = TaskTracker()