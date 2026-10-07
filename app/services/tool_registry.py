from collections.abc import Callable
from typing import Any


class ToolRegistry:

    def __init__(self):
        self._tools: dict[str, Callable[..., Any]] = {}

    def register(
        self,
        name: str,
        tool: Callable[..., Any],
    ) -> None:

        if name in self._tools:
            raise ValueError(
                f"Tool already registered: {name}"
            )

        self._tools[name] = tool

    def get(self, name: str) -> Callable[..., Any]:

        if name not in self._tools:
            raise KeyError(
                f"Tool not found: {name}"
            )

        return self._tools[name]

    def has(self, name: str) -> bool:
        return name in self._tools

    def list_tools(self) -> list[str]:
        return list(self._tools.keys())