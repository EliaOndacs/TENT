def _get_id(selector: str) -> str:
    if selector[0] == "#":
        return selector[1:]
    else:
        raise TypeError(f"`{selector}` is not valid selector")
