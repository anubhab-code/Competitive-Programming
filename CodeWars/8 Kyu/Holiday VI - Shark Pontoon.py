def shark(d1, d2, v1, v2, x):
    return "Alive!" if d1 / v1 < d2 / v2 * (x + 1) else "Shark Bait!"