from __future__ import annotations

from collections import defaultdict

from backend.framework.event import AgentEvent


class EventBus:

    def __init__(self):

        self._events = defaultdict(list)

    def publish(
        self,
        event: AgentEvent,
    ):

        self._events[event.agent].append(event)

    def events(
        self,
        agent: str,
    ):

        return self._events.get(agent, [])

    def all_events(self):

        events = []

        for value in self._events.values():

            events.extend(value)

        return events

    def count(self):

        return sum(len(v) for v in self._events.values())

    def clear(self):

        self._events.clear()


event_bus = EventBus()