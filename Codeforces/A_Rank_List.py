n,k=map(int,input().split())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append([-a,b])
l=sorted(l)
ans=l[k-1]
print(l.count(ans))