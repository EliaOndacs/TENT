import functools
from typing import Callable


def _IsSlot(func):
    return (hasattr(func, "IsSlot")) and (getattr(func, "IsSlot") == True)


class NotSlot(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Event:
    def __init__(self, _object, _signal) -> None:
        self.object = _object
        self.signal = _signal


class Signal:
    def __init__(self):
        self.slots: list[Callable] = []

    def connect(self, slot: Callable):
        if _IsSlot(slot):
            self.slots.append(slot)
        else:
            print(dir(slot))
            raise NotSlot(f"{slot!r} is not an slot!")

    def disconnect(self, slot: Callable):
        if _IsSlot(slot):
            self.slots.remove(slot)
        else:
            raise NotSlot(f"{slot!r} is not an slot!")

    def emit(self, sender, *args, **kwargs):
        for slot in self.slots:
            slot(Event(sender,self), *args, **kwargs)


def slot(func) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    setattr(wrapper, "IsSlot", True)
    return wrapper
