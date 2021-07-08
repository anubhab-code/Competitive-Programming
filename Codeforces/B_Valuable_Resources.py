n=int(input())
l,r,u,d=int(1e10),-int(1e10),-int(1e10),int(1e10)
for i in " "*n:
    x,y=map(int,input().split())
    l=min(l,y)
    r=max(y,r)
    u=max(u,x)
    d=min(d,x)
print(max((r-l)**2,(u-d)**2))