import re
def frame(balls):
    res = 0
    s = re.compile('(R|Y|G|Bn|Be|P|Bk|W)(\d*)')
    for c, i in re.findall(s, balls):
        if c == 'W':
            return 'Foul'
        if not i:
            num = 1
        else:
            num = int(i)
        res += blz[c]*num    
    return res if res <= 147 else 'invalid data'
        