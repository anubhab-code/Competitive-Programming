from collections import defaultdict
for _ in range(int(input())):
    n,m = map(int,input().split())
    check = defaultdict(int)
    temp = m+n
    temp-=2
    t2 = temp
    for i in range(n//2):
        t1 = t2
        for j in range(m//2):
            check[t1] += 4
            t1-=1
        if m%2==0:
            pass
        else:
            check[t1] += 2
        t2-=1
    if n%2==1:
        t1 = t2
        for j in range(m//2):
            check[t1] += 2
            t1-=1
        if m%2==0:
            pass
        else:
            check[t1] += 1
    ans = []
    t3= n//2 + m//2
    for i in range(t3,m+n-1):
        ans+=[i]*check[i]
    print(*ans)