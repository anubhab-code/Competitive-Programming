for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    ans,f,l,o=0,n,-1,0
    for i in range(n):
        if s[i]=='0':
            continue
        o+=1
        if f==n:
            f=i
        l=i
    if o and n-l-1<=k:
        ans+=1
        o-=1
        k-=n-l-1
    if o and f<=k:
        ans+=10
        o-=1
    ans+=11*o
    print(ans)