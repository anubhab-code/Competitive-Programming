def map_vector(vector, circle1, circle2):
    x0, y0 = vector
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    sc = r2/r1
    dx1, dy1 = x0-x1, y0-y1
    dx2, dy2 = sc*dx1, sc*dy1
    vector = x2+dx2, y2+dy2
    return vector