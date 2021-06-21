n,x=map(int,input().split())
t=1
final=0
for i in range(n):
    l,r=map(int,input().split())
    final+=((l-t)%x)+(r-l)+1
    t=r+1
print(final)