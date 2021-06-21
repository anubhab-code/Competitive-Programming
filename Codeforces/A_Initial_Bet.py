n=sum(list(map(int,input().split())))
if n%5 or n==0:
    print(-1)
else:
    print(n//5)
