def order_word(s):
    if not s:
        return "Invalid String!"
    return "".join(sorted(list(s)))