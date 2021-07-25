from collections import defaultdict as dd
n,k=map(int,input().split())
c=list(map(int,input().split()))
d=dd(int)
for i in c[:k]:
    d[i]+=1
f=len(d)
for i in range(k,n):
    _=i-k
    d[c[_]]-=1
    if d[c[_]]==0:
        del d[c[_]]
    d[c[i]]+=1
    if f<len(d):
        f=len(d)
print(f)