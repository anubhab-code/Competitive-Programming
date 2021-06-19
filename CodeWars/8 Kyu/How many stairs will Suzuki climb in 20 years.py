def stairs_in_20(stairs):
    tot = 0
    for d in stairs:
        for s in d:
            tot += s
    return tot * 20