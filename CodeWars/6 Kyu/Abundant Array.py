def d(n):
    s = sum(i for i in range(1,n//2+1) if not n%i)
    return (s-n,n) if s>n else None

def abundance(n):
    r = []
    i = 0
    while len(r) < n:
        x = d(i)
        if x:
            r.append(x)
        i += 1
    return [j for i,j in sorted(r)]