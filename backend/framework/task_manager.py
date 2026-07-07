from __future__ import annotations

from backend.framework.task import Task, TaskStatus


class TaskManager:

    def __init__(self):

        self._tasks: dict[str, Task] = {}

    def add(self, task: Task):

        self._tasks[task.id] = task

    def get(self, task_id: str):

        return self._tasks.get(task_id)

    def all(self):

        return list(self._tasks.values())

    def pending(self):

        return [
            task
            for task in self._tasks.values()
            if task.status == TaskStatus.PENDING
        ]

    def running(self):

        return [
            task
            for task in self._tasks.values()
            if task.status == TaskStatus.RUNNING
        ]

    def completed(self):

        return [
            task
            for task in self._tasks.values()
            if task.status == TaskStatus.COMPLETED
        ]

    def failed(self):

        return [
            task
            for task in self._tasks.values()
            if task.status == TaskStatus.FAILED
        ]

    def clear(self):

        self._tasks.clear()


task_manager = TaskManager()