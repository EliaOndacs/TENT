import functools
from typing import Callable, Generator
from dom import DOM, DOMContainer, DOMNode
from utils import push
from widgets import IsRenderable, Widget
from ids import _get_id

type MessagesResult = Generator[tuple | list, None, None]
type ComposeResult = Generator[Widget | tuple | list | set, None, None]


class App:
    def __init__(self) -> None:
        self._dom = DOM()

    def query_one(self, selector: str):
        return self._dom.query_one(selector)

    def query(self, selector: str):
        return self._dom.query(selector)

    def compose(self) -> ComposeResult:
        yield from ()

    def messages(self) -> MessagesResult:
        yield from ()

    def _pack(self):
        for item in self.compose():
            if isinstance(item, (tuple, list)):
                push(self._dom, DOMNode(item[0], _id=item[1]))
            else:
                push(self._dom, DOMNode(item))

    def _handle_messages(self):
        for message in self.messages():
            if isinstance(message, (tuple, list)):
                id_selector = message[0].split(".")[0]
                _objects = self.query(id_selector)
                message_ = message[0].split(".")[1]

                for _object in _objects:
                    if hasattr(_object, message_):
                        getattr(_object, message_).connect(message[1])
            elif isinstance(message, set):
                message = list[message]
                id_selector = message[0].split(".")[0]
                _objects = self.query(id_selector)
                message_ = message[0].split(".")[1]

                for _object in _objects:
                    if hasattr(_object, message_):
                        getattr(_object, message_).connect(message[1])

    def run(self):
        self._pack()
        self._handle_messages()
        for node in self._dom.nodes:
            if IsRenderable(node.widget):
                node.widget.render(node.depth)
