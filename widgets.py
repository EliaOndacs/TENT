import sys


from typing import Any, Callable

import ansi
import ansi.colour

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
    _validator: Callable|None = None

    def __init__(self, prompt: str, validator: Callable|None = None) -> None:
        """
        ## ARGS
            - prompt: Str -> prompt to be displayed
        """
        super().__init__()
        self.prompt = prompt
        self._validator = validator
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
        if self._validator:
            if self._validator(self.value) == True:
                self.Submitted.emit(sender=self)
            else:
                self.prompt = ansi.colour.fg.red + self.prompt + ansi.colour.fx.reset
                print(chr(7),end="")
                sys.stdout.write(f"{"\033[A"*len(self.prompt.split("\n"))}\33[2KT\r")
                sys.stdout.flush()
                self.render(depth)
        else:
            self.Submitted.emit(sender=self)


class Checkbox(Widget):

    _state: bool = False
    _prompt: str = ""

    def __init__(self, prompt) -> None:
        """
        An Checkbox widget that has a state property
        ## ARGS
            - prompt: Str -> prompt to be displayed
        """
        super().__init__()
        self.state: bool = False
        self.prompt = prompt
        self.Submitted = Signal()

    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, new: str):
        self._prompt = new

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new: bool):
        self._state = new

    def render(self, depth: int):
        key = ""
        print("\n")
        while key == "":
            sys.stdout.write("\033[A\033[A\33[2KT\r")
            sys.stdout.flush()
            print(f"{"    "*depth}[{'x' if self.state == True else ' '}] {self.prompt}", end="")
            key = input("\n")
            print(end="\b")
            if key == "":
                self.state = not self.state
        print("\033[A\033[A")
        self.Submitted.emit(sender=self)

class Label(Widget):

    _value: str = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new: str):
        self._value = new

    def render(self, depth: int):
        print(("    " * depth) + "╭"+("─"*(len(max(self.value.split("\n")))+1)))
        for line in self.value.splitlines():
            print(("    " * depth) + "| " + line)
        print(("    " * depth) + "╰"+("─"*(len(max(self.value.split("\n")))+1)))

    def __init__(self, text: str) -> None:
        """
        ## ARGS
            - text: Str -> text to be displayed
        """
        super().__init__()
        self.value = text
