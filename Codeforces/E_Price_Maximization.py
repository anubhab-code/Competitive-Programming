from collections import deque
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    ans,q = 0,[]
    for i in l:
        q.append([i%k,i])
    q.sort()
    q = deque(q)
    while q:
        a,ai = q.popleft()
        if q:
            if q[-1][0]+a < k:
                ans += ai//k
            else:
                b,bi = q.pop()
                ans += (ai+bi)//k
        else:
            ans += ai//k
    print(ans)