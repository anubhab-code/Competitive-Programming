for _ in range(int(input())):
    n,m,k = map(int,input().split())
    if m <= n//k:
        print(m)
    else:
        mx = n//k
        print(mx-((m-mx-1)//(k-1) + 1))