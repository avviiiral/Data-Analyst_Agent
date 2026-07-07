from __future__ import annotations

from collections import defaultdict

from backend.framework.message import AgentMessage


class MessageBus:

    def __init__(self):

        self._queues = defaultdict(list)

    def publish(
        self,
        message: AgentMessage,
    ) -> None:

        self._queues[message.receiver].append(message)

    def receive(
        self,
        agent_name: str,
    ) -> list[AgentMessage]:

        messages = self._queues[agent_name][:]

        self._queues[agent_name].clear()

        return messages

    def pending(
        self,
        agent_name: str,
    ) -> int:

        return len(self._queues[agent_name])

    def clear(self):

        self._queues.clear()


message_bus = MessageBus()