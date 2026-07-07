from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimelineEvent:
    timestamp: datetime
    agent: str
    event: str


class ExecutionTimeline:

    def __init__(self):
        self._events: list[TimelineEvent] = []

    def add(
        self,
        agent: str,
        event: str,
    ):
        self._events.append(
            TimelineEvent(
                timestamp=datetime.utcnow(),
                agent=agent,
                event=event,
            )
        )

    def events(self):
        return list(self._events)

    def clear(self):
        self._events.clear()


execution_timeline = ExecutionTimeline()