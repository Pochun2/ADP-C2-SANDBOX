def cap_in_range(value: int, lower: int, upper: int) -> int:
    if type(value) is not int or type(lower) is not int or type(upper) is not int:
        raise TypeError("All parameters must be exactly built-in int")
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value
