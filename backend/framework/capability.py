from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Capability:

    name: str

    description: str

    version: str = "1.0"

    tags: list[str] = field(default_factory=list)