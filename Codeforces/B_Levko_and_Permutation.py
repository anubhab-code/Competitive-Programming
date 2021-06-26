n,k = map(int,input().split())
l=[]
if n==k:
    print(-1)
else:
    for i in range(2,n-k+1):
        l.append(i)
    l.append(1)
    for j in range(n-k+1,n+1):
        l.append(j)
print(*l)