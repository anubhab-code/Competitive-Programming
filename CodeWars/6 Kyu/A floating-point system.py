def mant_exp(n, d):
    p = 0
    while n > 1:
            n /= 10
            p += 1
    while n < 1:
            n *= 10
            p -= 1
    return f"{int(n * 10 ** (d - 1))}P{p - d + 1}"

    