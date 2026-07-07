from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CollaborationContext:
    """
    Shared context between multiple agents during a single execution.
    """

    request: str = ""
    dataset: Any = None

    shared_memory: dict[str, Any] = field(default_factory=dict)

    results: dict[str, Any] = field(default_factory=dict)

    history: list[str] = field(default_factory=list)

    def add_result(
        self,
        agent: str,
        result: Any,
    ) -> None:

        self.results[agent] = result
        self.history.append(agent)

    def get_result(
        self,
        agent: str,
    ):

        return self.results.get(agent)