ca=[0]*100007
cb=[0]*100007
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        ca[(a[i]+1)//2]=i
        cb[b[i]//2]=i
    for i in range(2,n+1):
        ca[i]=min(ca[i],ca[i-1])
    for i in range(n-1,2,-1):
        cb[i]=min(cb[i],cb[i+1])
    ans=n+n
    for i in range(1,n+1):
        ans=min(ans,ca[i]+cb[i])
    print(ans)
        