"""
        **Tent Python Application Framework**
        MIT License Copyright (c) 2024 EliaOndacs
          developed and made by EliaOndacs
"""

from app import App, ComposeResult, MessagesResult
from signals import slot
from widgets import Text, Input


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Text("hello, user! what is your name?")
        yield {Input("enter your name: "), "user_name"}
        yield {Text(f"hello, user!"), "text"}

    @slot
    def test_function(self, event):
        self.query_one("#text").value = f"hello, {event.object.ReturnValue}!"
        event.signal.disconnect(self.test_function)

    def messages(self) -> MessagesResult:
        yield ["#user_name.Submitted", self.test_function]


def main():

    MyApp().run()


# end main()

if __name__ == "__main__":
    main()
# end main
