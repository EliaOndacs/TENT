"""
        **Tent Python Application Framework**
        MIT License Copyright (c) 2024 EliaOndacs
          developed and made by EliaOndacs
"""

from dom import DOM, DOMNode
from utils import push
from widgets import IsRenderable, Text


def main():

    dom = DOM()
    push(dom, DOMNode(Text("hello, world!"),"test",2))
    # finish this


# end main()

if __name__ == "__main__":
    main()
# end main
