from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Worker:

    id: int

    busy: bool = False

    current_agent: str | None = None

    def assign(
        self,
        agent_name: str,
    ) -> None:

        self.busy = True

        self.current_agent = agent_name

    def release(self) -> None:

        self.busy = False

        self.current_agent = None