def cost_estimate_line(tokens: int, credit_micro: int, api_usd_micro: int) -> str:
    for value in (tokens, credit_micro, api_usd_micro):
        if type(value) is not int:
            raise TypeError("inputs must be exact integers")
    for value in (tokens, credit_micro, api_usd_micro):
        if value < 0:
            raise ValueError("inputs must be nonnegative")
    return f"tokens={tokens};credit_eq_micro={credit_micro};api_usd_eq_micro={api_usd_micro};billing=ESTIMATE_NOT_ACTUAL"
