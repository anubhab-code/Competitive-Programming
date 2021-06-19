from math import *
def solution(a, b, c) :
    c *= pi/180;
    d = a + b * cos(c)
    e = b * sin(c)
    return [hypot(d, e), atan2(e,d) * 180 / pi]