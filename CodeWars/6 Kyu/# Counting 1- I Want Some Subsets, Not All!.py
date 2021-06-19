def f(n):
    c, b = 0, 1
    for _ in range(n):
        c, b = b, c + b + 1
    return c