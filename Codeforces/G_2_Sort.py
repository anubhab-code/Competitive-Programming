for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    check = []
    for i in range(n-1):
        if 2*a[i+1] > a[i]:
            check.append(1)
        else:
            check.append(0)
    ans,sa = 0,sum(check[:k])
    for i in range(k,n-1):
        if sa==k:
            ans += 1
        sa -= check[i-k]
        sa += check[i]
    if sa==k:
        ans += 1
    print(ans)