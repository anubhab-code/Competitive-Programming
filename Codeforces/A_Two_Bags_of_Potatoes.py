y,k,n=map(int,input().split())
x=k-y%k
maxm=n-y
l=[]
if x<=maxm:
    while x<=maxm:
        l.append(x)
        x+=k
    print(*l)
else:
    print(-1)