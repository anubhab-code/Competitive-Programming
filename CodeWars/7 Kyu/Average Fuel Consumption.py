def solve(before, after):
    (avg1, dist1), (avg2, dist2) = before, after
    return round((avg2 * dist2 - avg1 * dist1) / (dist2 - dist1), 1)