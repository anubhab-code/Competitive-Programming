import re
def find_longest_substr(s):
    i = 0
    t = ()
    for j in re.finditer(r'(([a-zA-Z0-9])\2*)',s):
        if len(j.group())>i:
            i = len(j.group())
            t = (str(ord(j.group()[0])),[j.start(),j.end()-1])
    return [t[0],i,t[1]]