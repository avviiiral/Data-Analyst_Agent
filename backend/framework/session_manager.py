from __future__ import annotations

from backend.framework.agent_session import AgentSession


class SessionManager:

    def __init__(self):

        self._sessions: dict[str, AgentSession] = {}

    def create(self) -> AgentSession:

        session = AgentSession()

        self._sessions[session.id] = session

        return session

    def get(
        self,
        session_id: str,
    ) -> AgentSession | None:

        return self._sessions.get(session_id)

    def exists(
        self,
        session_id: str,
    ) -> bool:

        return session_id in self._sessions

    def remove(
        self,
        session_id: str,
    ):

        self._sessions.pop(session_id, None)

    def clear(self):

        self._sessions.clear()

    def count(self):

        return len(self._sessions)

    def ids(self):

        return sorted(self._sessions.keys())


session_manager = SessionManager()