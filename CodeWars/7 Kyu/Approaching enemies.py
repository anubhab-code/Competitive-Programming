def calculate_time(p1, p2):
    x0, y0 = p1
    x1, y1 = p2
    v = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** .5 / 5
    d = (x1 ** 2 + y1 ** 2) ** .5
    return round(d/v, 3)