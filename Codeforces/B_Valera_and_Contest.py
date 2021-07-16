import math
n,k,l,r,sall,sk = map(int,input().split())
osk,ok = sk,k
ans = []
while k:
    x = math.ceil(sk/k)
    ans.append(x)
    k -= 1
    sk -= x
v = n-ok
sall -= osk
while v:
    x = math.ceil(sall/v)
    ans.append(x)
    v -= 1
    sall -= x
print(*ans)