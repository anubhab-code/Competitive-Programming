def combine(*bs):
    c = {}
    for b in bs:
        for k, v in b.items():
            c[k] = v + c.get(k, 0)
    return c