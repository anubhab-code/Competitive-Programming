def determineTime(arr):
    totalSec = 0
    for a in arr:
        (h, m, s) = a.split(':')
        totalSec += (int(h) * 3600 + int(m) * 60 + int(s))
    return (24 * 60 * 60) > totalSec