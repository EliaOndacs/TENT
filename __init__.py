"""
        **Tent Python Application Framework**
        MIT License Copyright (c) 2024 EliaOndacs
          developed and made by EliaOndacs
"""

from app import App, ComposeResult
from widgets import Label, Text, Widget


class MyWidget(Widget):
    def render(self, depth: int) -> None:
        print(f"depth:{depth}")


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Text("hello, world!")


def main():

    MyApp().run()

    return


if __name__ == "__main__":
    main()
# endif
