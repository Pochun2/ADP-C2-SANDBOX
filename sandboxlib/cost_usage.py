def sum_settled_tokens(records: list[tuple[str, int]]) -> int:
    if type(records) is not list:
        raise TypeError("records must be a list")
    seen = set()
    total = 0
    for record in records:
        if type(record) is not tuple:
            raise TypeError("each record must be a tuple")
        if len(record) != 2:
            raise TypeError("each record must contain exactly two items")
        invocation_id, tokens = record
        if type(invocation_id) is not str:
            raise TypeError("invocation_id must be a string")
        if type(tokens) is not int:
            raise TypeError("tokens must be an exact int")
        if not invocation_id:
            raise ValueError("invocation_id must not be empty")
        if tokens < 0:
            raise ValueError("tokens must be nonnegative")
        if invocation_id in seen:
            raise ValueError("duplicate invocation_id")
        seen.add(invocation_id)
        total += tokens
    return total
