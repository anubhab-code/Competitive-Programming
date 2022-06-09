n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(1,n+1):
    d[l[i-1]]=i
v,p=0,0

m=int(input())
t1=list(map(int,input().split()))
for i in range(m):
    t=t1[i]
    v+=d[t]
    p+=(n+1-d[t])
print(v,p)
