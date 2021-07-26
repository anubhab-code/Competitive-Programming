import collections as cc
import math as mt
I=lambda:list(map(int,input().split()))
n,=I()
l=I()
f=cc.Counter(l)
ans=[]
for i in range(n):
    now=max(f)
    f[now]-=1
    for j in ans:
        f[mt.gcd(now,j)]-=2
    ans.append(now)
    f+=cc.Counter()
print(*ans)