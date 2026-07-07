from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentContext:
    dataset: Any | None = None
    memory: dict[str, Any] = field(default_factory=dict)

    collaboration: Any | None = None

    def result(self, agent: str):
        if self.collaboration is None:
            return None
        return self.collaboration.get_result(agent)

@dataclass
class AgentResponse:
    success: bool
    agent: str
    message: str
    data: Any = None


class BaseAgent(ABC):

    name: str = "BaseAgent"

    @abstractmethod
    def run(
        self,
        context: AgentContext,
    ) -> AgentResponse:
        ...