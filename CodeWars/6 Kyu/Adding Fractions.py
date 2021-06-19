from fractions import Fraction
def add_fracs(*args): 
    if not args:
        return ''
    s=0
    for arg in args:
        s+=Fraction(arg)
    return str(s)