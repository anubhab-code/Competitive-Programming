def mpg2lp100km(mpg):
    g = 3.785411784
    m = 1.609344
    
    return round(100 / ((mpg * m)/g),2)
    
def lp100km2mpg(lp100km):
    g = 3.785411784
    m = 1.609344
    
    return round((100/m) / (lp100km/g),2)