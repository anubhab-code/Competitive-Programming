def combine(*args):
    L = max(len(i) for i in args)
    a = []
    j = 0
    while j<L:
        for i in args:
            try:
                a.append(i[j])
            except:
                pass
        j += 1
    return a