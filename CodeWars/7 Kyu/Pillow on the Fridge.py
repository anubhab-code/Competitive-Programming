def pillow(s):
    s1, s2 = s
    for i in range(len(s1)):
        if s1[i] == 'n' and s2[i] == 'B':
            return True
    return False