from typing import Any

from ids import _get_id
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
        self._nodes: list[DOMNode] = []

    def __push__(self, object: DOMNode):
        if isinstance(object, DOMNode):
            self._nodes.append(object)

    @property
    def nodes(self):
        yield from self._nodes

    def query_one(self, selector: str):
        _id = _get_id(selector)
        for node in self.nodes:
            if node.id == _id:
                return node.widget
        return None

    def query(self, selector: str) -> list:
        _id = _get_id(selector)
        return [node.widget for node in self.nodes if node.id == _id]
