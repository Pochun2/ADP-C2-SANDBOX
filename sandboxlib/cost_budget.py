def budget_tokens_remaining(limit: int, settled: int, reserved: int) -> int:
    for value in (limit, settled, reserved):
        if type(value) is not int:
            raise TypeError("Budget values must be exact integers")
        if value < 0:
            raise ValueError("Budget values must be nonnegative")
    if settled + reserved > limit:
        raise ValueError("Settled and reserved tokens exceed the limit")
    return limit - settled - reserved
