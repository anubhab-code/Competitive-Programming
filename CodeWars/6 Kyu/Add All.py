def add_all(a):
    r = t = 0
    while len(a) > 1:
        a = sorted(a)
        r = sum(a[:2])
        t += r
        a = a[2:] + [r]
    return t