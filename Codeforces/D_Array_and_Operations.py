for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l=sorted(l)[::-1]
    ans = sum(l[2*k:])
    for i in range(k,2*k):
        ans+=int(l[i]//l[i-k])
    print(ans)
        