n,s,t=map(int,input().split())
l=list(map(int,input().split()))
ans=0
check=s
while check!=t and l[check-1]!=0:
    b=l[check-1]
    l[check-1]=0
    check=b
    ans+=1
if check==t:
    print(ans)
else:
    print(-1)