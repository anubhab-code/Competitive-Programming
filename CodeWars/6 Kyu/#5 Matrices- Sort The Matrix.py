def order(m):
    g = iter(sorted([ e for l in m for e in l ]))
    return [ [next(g) for x in range(len(m[0]))] for y in range(len(m)) ]