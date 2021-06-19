import re
def alphabet_war(fight):
    l = {"w":4,"p":3,"b":2,"s":1}
    r = {"m":4,"q":3,"d":2,"z":1}
    left=0;right=0
    s=re.sub(r'.?\*+.?','',fight)
    right=sum([r.get(i,0) for i in s])
    left =sum([l.get(i,0) for i in s])
    if right==left:
        return "Let's fight again!"
    elif right>left:
        return "Right side wins!"
    else:
        return "Left side wins!"