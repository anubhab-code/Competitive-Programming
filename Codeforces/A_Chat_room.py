n = input()
try:
    h = n.index('h')
    n = n[h+1:]
    e = n.index('e')
    n = n[e+1:]
    l = n.index('l')
    n = n[l+1:]
    l = n.index('l')
    n = n[l+1:]
    o = n.index('o')
    print("YES")
except :
    print("NO")