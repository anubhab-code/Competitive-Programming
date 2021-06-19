def generator (a, b, step):
    if step == 0: return []
    return range(a, b+1, step) if a <= b else range(a, b-1, -step)