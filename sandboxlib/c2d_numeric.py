def clamp_nonnegative(value: int, ceiling: int) -> int:
    if type(value) is not int or type(ceiling) is not int:
        raise TypeError("expected int")
    return min(max(value, 0), max(ceiling, 0))
