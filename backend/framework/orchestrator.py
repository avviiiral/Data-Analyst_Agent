from __future__ import annotations

from backend.framework.base_agent import (
    AgentContext,
    AgentResponse,
)
from backend.framework.registry import registry
from backend.framework.task import Task, TaskStatus
from backend.framework.collaboration import CollaborationContext
from datetime import datetime

from backend.framework.execution_history import (
    execution_history,
    ExecutionRecord,
)

from backend.framework.agent_metrics import agent_metrics

class AgentOrchestrator:

    def execute(
        self,
        task: Task,
    ) -> AgentResponse:

        if task.assigned_agent is None:
            raise ValueError("No agent assigned to task.")

        if not registry.exists(task.assigned_agent):
            raise ValueError(
                f"{task.assigned_agent} is not registered."
            )

        collaboration = task.payload.setdefault(
            "collaboration",
            CollaborationContext(
                dataset=task.payload.get("dataset"),
            ),
        )

        # Verify dependency completion
        for dependency in task.dependencies:

            if collaboration.get_result(dependency) is None:

                raise RuntimeError(
                    f"Dependency '{dependency}' has not executed yet."
                )

        task.status = TaskStatus.RUNNING

        try:

            agent = registry.create(task.assigned_agent)

            response = agent.run(
                AgentContext(
                    dataset=task.payload.get("dataset"),
                    memory=task.payload,
                    collaboration=collaboration,
                )
            )

            collaboration.add_result(
                task.assigned_agent,
                response.data,
            )
            execution_history.add(
                ExecutionRecord(
                    timestamp=datetime.utcnow(),
                    agent=task.assigned_agent,
                    success=response.success,
                    message=response.message,
                    data=response.data,
                )
            )
            
            agent_metrics.record(
                agent=task.assigned_agent,
                success=True,
            )

            task.status = TaskStatus.COMPLETED
            task.result = response.data

            return response

        except Exception as e:

            task.status = TaskStatus.FAILED
            task.error = str(e)
            execution_history.add(
                ExecutionRecord(
                    timestamp=datetime.utcnow(),
                    agent=task.assigned_agent,
                    success=False,
                    message=str(e),
                )
            )
            agent_metrics.record(
                agent=task.assigned_agent,
                success=False,
            )
            
            raise

orchestrator = AgentOrchestrator()