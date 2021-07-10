n,k=map(int,input().split())
m=n
ans=0
while n:
    ans+=1
    n//=2
if k==1:
    print(m)
else:
    print(2**ans-1)