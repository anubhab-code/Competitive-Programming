def akey(a):
    if a.islower():
        return ord(a)
    else:
        return ord(a)+32
def alphabetized(s):
    s = ''.join(s.split())
    m = sorted(s, key=akey)
    return ''.join([i for i in m if i.isalpha()])