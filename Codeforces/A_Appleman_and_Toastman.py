n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
ans=sum(l)
r=ans
for i in range(n-1):
    r-=l[i]
    ans+=l[i]
    ans+=r
print(ans)