import bisect
n,x = map(int,input().split())
a = sorted(map(int,input().split()))
ans = 0
if a[(n-1)//2] != x:
    while a[(n-1)//2] != x:
        a.insert(bisect.bisect_right(a,x),x)
        ans+=1
        n+=1
print(ans)