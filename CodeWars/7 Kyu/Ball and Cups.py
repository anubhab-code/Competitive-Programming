def cup_and_balls(b, arr):
    for l, r in arr:
        b = r if b == l else l if b == r else b
    return b