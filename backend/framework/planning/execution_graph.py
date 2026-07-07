from __future__ import annotations

from collections import defaultdict

from backend.framework.planning.task import PlanningTask


class ExecutionGraph:

    def __init__(self):

        self.nodes: dict[str, PlanningTask] = {}

        self.edges = defaultdict(list)

    def build(
        self,
        tasks: list[PlanningTask],
    ):

        self.nodes.clear()

        self.edges.clear()

        for task in tasks:

            self.nodes[task.name] = task

        for task in tasks:

            for dependency in task.dependencies:

                self.edges[dependency].append(task.name)

        return self

    def successors(
        self,
        task_name: str,
    ):

        return self.edges.get(task_name, [])

    def predecessors(
        self,
        task_name: str,
    ):

        return self.nodes[task_name].dependencies

    def roots(self):

        return [
            task.name
            for task in self.nodes.values()
            if not task.dependencies
        ]

    def leaves(self):

        return [
            task
            for task in self.nodes
            if task not in self.edges
        ]


execution_graph = ExecutionGraph()