def validate_ean(code):
    code = map(int, code)
    return (sum(code[0::2]) + sum(code[1::2]) * 3) % 10 == 0