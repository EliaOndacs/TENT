from typing import Any

from widgets import Widget


class DOMNode:
    def __init__(self, widget: Widget, _id: str | None = None, depth: int = 0) -> None:
        self.widget: Widget = widget
        self.id: str | None = _id
        self._depth: int = depth
        self._attributes: dict[str, Any] = {}

    @property
    def attributes(self):
        return self._attributes

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, new: int):
        self._depth = new

    def __setitem__(self, name, value):
        self.attributes.__setitem__(name, value)

    def __getitem__(self, name):
        self.attributes.__getitem__(name)


class DOM:
    def __init__(self) -> None:
        self.nodes: list[DOMNode] = []

    def __push__(self, object: DOMNode):
        if isinstance(object, DOMNode):
            self.nodes.append(object)
