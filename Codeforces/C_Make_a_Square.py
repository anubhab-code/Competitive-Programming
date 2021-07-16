import sys
from itertools import combinations
n = int(input())
s = list(str(n))
x = len(s)
l = []
for i in range(len(s)):
    l.append(i)
ans = 10000
for i in range(1,x+1):
    for j in combinations(l,i):
        u = []
        for k in j:
            u.append(s[k])
        p = "".join(u)
        if p[0] == "0":
            continue
        m = int(p)
        m = m**0.5
        h = int(m)
        if h == m:
            w = x-i
            if w < ans:
                ans = w
if ans == 10000:
    ans = -1
print(ans)