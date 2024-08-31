

def push(object, child):
    if hasattr(object,"__push__"):
        object.__push__(child)
    else:
        raise AttributeError(f"{object!r} dose not support pushing an object to it")
