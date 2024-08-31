from typing import Any

from signals import Signal


def IsRenderable(obj: Any):
    return hasattr(obj, "render")


class Widget:
    def render(self, depth: int) -> None: ...


class Text(Widget):

    _value: str = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new: str):
        self._value = new

    def render(self, depth: int):
        print(("    " * depth) + self.value)

    def __init__(self, text: str) -> None:
        """
        ## ARGS
            - text: Str -> text to be displayed
        """
        super().__init__()
        self.value = text


class Input(Widget):

    _prompt: str = ""

    def __init__(self, prompt: str) -> None:
        """
        ## ARGS
            - prompt: Str -> prompt to be displayed
        """
        super().__init__()
        self.prompt = prompt
        self.value: str = ""
        self.Submitted = Signal()

    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, new: str):
        self._prompt = new

    @property
    def ReturnValue(self):
        return self.value

    def render(self, depth: int):
        self.value = input(("    " * depth) + self.prompt)
        self.Submitted.emit(sender=self)
