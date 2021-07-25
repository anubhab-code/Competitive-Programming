cost=1000000001
n=int(input())
for i in range(n):
    a,p,x=list(map(int,input().split()))
    if a>=x:
        pass
    elif p<cost:
        cost=p
        
if cost==1000000001:
    print(-1)
else:
    print(cost)