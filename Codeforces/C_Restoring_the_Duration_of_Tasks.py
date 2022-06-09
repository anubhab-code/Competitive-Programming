for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans,p = [],0
    for i in range(n):
        t = max(p,a[i])
        t1 = b[i]-t
        ans.append(t1)
        p = b[i]
    print(*ans)