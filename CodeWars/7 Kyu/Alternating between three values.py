def f(x, a, b, c):
    arr = a, b, c, a
    return arr[ arr.index(x) + 1 ]