import functools
from typing import Callable, Generator
from dom import DOM, DOMNode
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

    def compose(self) -> ComposeResult: ...
    def messages(self) -> MessagesResult: ...

    def _pack(self):
        for item in self.compose():
            if isinstance(item, (tuple, list)):
                push(self._dom, DOMNode(item[0], _id=item[1]))
            elif isinstance(item, set):
                item = list(item)
                push(self._dom, DOMNode(item[0], _id=item[1]))
            else:
                push(self._dom, DOMNode(item))

    def _handle_messages(self):
        for message in self.messages():
            if isinstance(message, (tuple, list)):
                id_selector = message[0].split(".")[0]
                objects = self.query(id_selector)
                message_ = message[0].split(".")[1]

                for object in objects:
                    if hasattr(object, message_):
                        getattr(object,message_).connect(message[1])
            elif isinstance(message, set):
                message = list[message]
                id_selector = message[0].split(".")[0]
                objects = self.query(id_selector)
                message_ = message[0].split(".")[1]

                for object in objects:
                    if hasattr(object, message_):
                        getattr(object,message_).connect(message[1])

    def run(self):
        self._pack()
        self._handle_messages()
        for node in self._dom.nodes:
            if IsRenderable(node.widget):
                node.widget.render(node.depth)


# def on(MessageType: str, app: App):

#     def decorator(function: Callable):
#         objects = app.query(_get_id(MessageType.split(".")[0]))
#         message = MessageType.split(".")[1]

#         for object in objects:
#             getattr(object, message).connect(function)

#         @functools.wraps(function)
#         def wrapper(*args, **kwargs):
#             return function(*args, **kwargs)

#         return wrapper

#     return decorator
