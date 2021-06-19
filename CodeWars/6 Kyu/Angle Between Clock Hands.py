from math import pi
def hand_angle(hours, minutes):
    ah=(pi/6)*hours
    am=(pi/30)*minutes
    if minutes:
        ah+=am/12
    a=abs(ah-am)
    return a if a<=pi else 2*pi-a  