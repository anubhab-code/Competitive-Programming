n,m=map(int,input().split())
minm=(n+1)//2
final=((minm+m-1)//m)*m
if final>n:
    print(-1)
else:
    print(final)