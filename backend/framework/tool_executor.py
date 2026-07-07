from __future__ import annotations

from backend.framework.tool_registry import tool_registry


class ToolExecutor:

    @staticmethod
    def execute(
        tool_name: str,
        *args,
        **kwargs,
    ):

        return tool_registry.execute(
            tool_name,
            *args,
            **kwargs,
        )

    @staticmethod
    def available_tools():

        return tool_registry.names()

    @staticmethod
    def exists(
        tool_name: str,
    ):

        return tool_registry.get(tool_name) is not None