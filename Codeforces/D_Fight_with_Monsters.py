import math
n,a,b,k = map(int,input().split())
l = list(map(int,input().split()))
ans=0
for i in range(n):
    l[i]=l[i]%(a+b)
    if l[i]==0:
        l[i]=a+b
l=sorted(l)
# print(l)
for j in l:
    if j>0:
        if k>=math.ceil(j/a)-1:
            ans+=1
            k-=math.ceil(j/a)-1
print(ans)