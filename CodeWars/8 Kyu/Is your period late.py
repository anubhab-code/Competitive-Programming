import datetime
def period_is_late(last,today,c):
    d = (today - last).days
    return d > c 