from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4
from typing import Any


@dataclass
class AgentEvent:

    agent: str

    event_type: str

    data: dict[str, Any] = field(default_factory=dict)

    id: str = field(default_factory=lambda: str(uuid4()))

    timestamp: datetime = field(default_factory=datetime.utcnow)