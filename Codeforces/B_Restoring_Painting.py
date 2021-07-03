n,a,b,c,d = map(int,input().split())
ans = 0
for i in range(1,n+1):
    p = i+b-c
    q = i+a+b-c-d
    r = i+a-d
    if 1<=p<=n and 1<=q<=n and 1<=r<=n:
        ans+=1
print(ans*n)