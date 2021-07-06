n,h = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l)
for i in range(n):
    if l[i]<0 and h>0:
        l[i]=abs(l[i])
        h-=1
if h%2==0:
    print(sum(l))
else:
    print(sum(l)-(2*min(l)))