p,q,l,r=map(int,input().split())
x=[]
y=[]
for i in range(p):
    u,v=map(int,input().split())
    x.extend(i for i in range(u,v+1))
for i in range(q):
    u,v=map(int,input().split())
    y.extend(i for i in range(u,v+1))
x=set(x)
y=set(y)
ans=0
for i in range(l,r+1):
    for j in y:
        if j+i in x:
            ans+=1
            break
print(ans)