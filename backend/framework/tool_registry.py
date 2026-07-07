from __future__ import annotations

from backend.framework.tool import Tool


class ToolRegistry:

    def __init__(self):

        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool):

        self._tools[tool.name] = tool

    def get(self, name: str):

        return self._tools.get(name)

    def names(self):

        return sorted(self._tools.keys())

    def execute(self, name: str, *args, **kwargs):

        tool = self.get(name)

        if tool is None:
            raise ValueError(f"Tool '{name}' not found.")

        return tool.function(*args, **kwargs)

    def clear(self):

        self._tools.clear()


tool_registry = ToolRegistry()