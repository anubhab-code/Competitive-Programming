for _ in range(int(input())):
    n = int(input())
    r1 = list(map(int,input().split()))
    r2 = list(map(int,input().split()))
    for i in range(1,n):
        r1[i] += r1[i-1]
    for i in range(n-2,-1,-1):
        r2[i] += r2[i+1]
    ans = float('inf')
    for i in range(n):
        temp = 0
        if i < (n-1):
            temp = max(r1[-1]-r1[i],temp)
        if i > 0:
            temp = max(temp,r2[0]-r2[i])
        ans = min(ans,temp)
    print(ans)