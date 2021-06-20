n,m=map(int,input().split())
ans=0
l=list(map(int,input().split()))
p=m-1
if l[p]==1:
    ans+=1
q=max(m-1,n-m)
for i in range(1,q+1):
    if p+i<=n-1 and p-i>=0:
        if l[p+i]+l[p-i]==2:
            ans+=2
    elif p+i>n-1 and p-i>=0:
        if l[p-i]==1:
            ans+=1
    elif p+i<=n-1 and p-i<0:
        if l[p+i]==1:
            ans+=1
print(ans)