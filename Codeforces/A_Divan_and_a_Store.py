for _ in range(int(input())):
    n,l,r,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        if a[i]>=l and a[i]<=r:
            ans.append(a[i])
    ans=sorted(ans)
    j = 0
    n = len(ans)
    final = 0
    while j<n:
        if k-ans[j]<0:
            break
        else:
            final+=1
            k-=ans[j]
            j+=1
    print(final)