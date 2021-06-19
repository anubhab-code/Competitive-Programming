def find_slope(points):
    x, y, x2, y2 = points
    try:
        return str(int((y2 - y) / (x2 - x)))
    except ZeroDivisionError:
        return 'undefined'