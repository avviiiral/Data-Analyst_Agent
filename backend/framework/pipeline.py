from __future__ import annotations

from backend.framework.orchestrator import orchestrator
from backend.framework.planner import planner
from backend.framework.task import Task
from backend.framework.execution_dag import execution_dag
from backend.framework.execution_graph import execution_graph


class AgentPipeline:

    """
    Planner -> Assign Agent -> Execute
    """

    AGENT_MAPPING = {
        "Profile Dataset": "DataAgent",
        "Statistics": "StatisticsAgent",
        "Correlation": "CorrelationAgent",
        "Visualization": "VisualizationAgent",
        "Insights": "InsightAgent",
        "Forecast": "ForecastAgent",
        "General Analysis": "DataAgent",
    }

    def run(
        self,
        request: str,
        dataset=None,
    ):

        tasks = planner.plan(request)

        results = []

        for task in tasks:

            task.payload["dataset"] = dataset

            task.assigned_agent = self.AGENT_MAPPING.get(
                task.name,
                "DataAgent",
            )
        graph = execution_graph.build(tasks)

        levels = execution_dag.build(tasks)

        for level in levels:

            # Parallel execution will be added later.
            for task in level:

                results.append(
                    orchestrator.execute(task)
                )

        return {
            "graph": graph,
            "results": results,
        }

pipeline = AgentPipeline()