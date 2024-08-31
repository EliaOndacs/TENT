"""
        **Tent Python Application Framework**
        MIT License Copyright (c) 2024 EliaOndacs
          developed and made by EliaOndacs
"""

from app import App, ComposeResult, MessagesResult
from signals import slot
from widgets import Text, Input
from ansi.colour import *


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Text(f"hello, user!\n{fg.yellow}what is your name?")
        yield Input(f"\t{fx.reset+fx.blink}:{fx.reset+fg.cyan}"), "user_name"
        yield Text(f"NULL"), "text"

    def messages(self) -> MessagesResult:
        yield ["#user_name.Submitted", self.test_function]

    @slot
    def test_function(self, event):
        msg = f"{fx.reset}hello, {fg.green}{event.object.ReturnValue}{fx.reset}!"
        self.query_one("#text").value = msg


def main():

    MyApp().run()

    return


if __name__ == "__main__":
    main()
# endif
