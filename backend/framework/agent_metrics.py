from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AgentMetric:
    executions: int = 0
    successes: int = 0
    failures: int = 0


class AgentMetrics:

    def __init__(self):
        self._metrics: dict[str, AgentMetric] = {}

    def record(
        self,
        agent: str,
        success: bool,
    ):

        metric = self._metrics.setdefault(
            agent,
            AgentMetric(),
        )

        metric.executions += 1

        if success:
            metric.successes += 1
        else:
            metric.failures += 1

    def get(
        self,
        agent: str,
    ):

        return self._metrics.get(
            agent,
            AgentMetric(),
        )

    def all(self):

        return self._metrics


agent_metrics = AgentMetrics()