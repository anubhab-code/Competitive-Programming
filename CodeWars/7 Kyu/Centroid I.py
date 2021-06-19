from numpy import mean

def centroid(c):
    x = round(mean([p[0] for p in c]), 2)
    y = round(mean([p[1] for p in c]), 2)
    z = round(mean([p[2] for p in c]), 2)
    return [x, y, z]