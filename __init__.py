"""
        **Tent Python Application Framework**
        MIT License Copyright (c) 2024 EliaOndacs
          developed and made by EliaOndacs
"""

from app import App, ComposeResult, MessagesResult
from signals import slot
from widgets import Checkbox, Label, Text, Input
from ansi.colour import *

def IsNumber(value: str):
    return value.isnumeric()
class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Input("enter a number: ",validator=IsNumber), "test"

    def messages(self) -> MessagesResult:
        yield ["#test.Submitted", self.test_function]

    @slot
    def test_function(self, event):
        print(f"current value is {int(event.object.ReturnValue)}")


def main():

    MyApp().run()

    return


if __name__ == "__main__":
    main()
# endif
