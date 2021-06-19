for _ in range(int(input())):
    n,m,i,j=map(int,input().split())
    l=[]
    if i>=n/2 and j>=m/2:
        l.append(1)
        l.append(m)
        l.append(n)
        l.append(1)
        print(*l)
    elif i<=n/2 and j<=m/2:
        l.append(1)
        l.append(m)
        l.append(n)
        l.append(1)
        print(*l)
    else:
        l.append(1)
        l.append(1)
        l.append(n)
        l.append(m)
        print(*l)