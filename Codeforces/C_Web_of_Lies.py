from collections import defaultdict
from sys import stdin
n,m = map(int,stdin.readline().split())
d,ss = defaultdict(set),set()
for i in range(1, n+1):
    ss.add(i)
for i in range(m):
    a,b=map(int,stdin.readline().split())
    ma,mi=max(a,b),min(a,b)
    d[mi].add(ma)
    if mi in ss:
        ss.remove(mi)
q = int(stdin.readline())
for i in range(q):
    l = list(map(int,stdin.readline().split()))
    if l[0]!=1 and l[0]!=2:
        print(len(ss))
    elif l[0]==2:
        a,b= l[1],l[2]
        mi=min(a,b)
        ma=max(a,b)
        d[mi].add(ma)
        d[mi].remove(ma)
        if not len(d[mi]):
            ss.add(mi)
    elif l[0]==1:
        b,a=l[2],l[1]
        ma,mi=max(a,b),min(a,b)
        d[mi].add(ma)
        if mi in ss:
            ss.remove(mi)