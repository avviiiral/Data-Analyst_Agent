from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExecutionNode:
    agent: str
    dependencies: list[str] = field(default_factory=list)


class ExecutionGraph:

    def build(self, tasks):

        nodes = []

        for task in tasks:

            nodes.append(
                ExecutionNode(
                    agent=task.assigned_agent,
                    dependencies=list(task.dependencies),
                )
            )

        return nodes


execution_graph = ExecutionGraph()