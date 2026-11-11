def ascii_compact(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    result = ""
    pending_space = False
    for ch in value:
        if ord(ch) > 127:
            raise ValueError("non-ASCII characters are not permitted")
        if ch in " \t\r\n\v\f":
            if result:
                pending_space = True
        else:
            if pending_space:
                result += "-"
            result += ch.lower()
            pending_space = False
    if not result:
        raise ValueError("normalized result is empty")
    return result
