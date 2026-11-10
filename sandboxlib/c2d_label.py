def label_key(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("value must be str")
    value = value.strip().lower()
    if not value:
        raise ValueError("empty label")
    while "  " in value:
        value = value.replace("  ", " ")
    return value.replace(" ", "_")
