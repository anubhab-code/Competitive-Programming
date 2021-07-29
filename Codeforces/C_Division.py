for _ in range(int(input())):
    p,q = map(int,input().split())
    ans = q
    l=[]
    j=2
    while j*j <= ans:
        if ans%j == 0:
            l.append(j)
            while ans%j == 0:
                ans //= j
        j += 1
    if ans>1:
        l.append(ans)
        ans = 1
    for k in l:
        y = p
        while y%q == 0:
            y //= k
        ans = max(ans,y)
    print(ans)