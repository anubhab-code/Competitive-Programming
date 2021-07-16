n,k=map(int,input().split())
l=[0]*11
ans=0
for x in input().split():
    t=int(x)
    l[10-t%10]+=1
    ans+=t//10
for i in range(1,10):
    t=min(k//i,l[i])
    ans+=t
    k-=t*i
t=k//10
ans+=min(t,n*10-ans)
print(ans)