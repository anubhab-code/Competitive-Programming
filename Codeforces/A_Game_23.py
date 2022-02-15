m,n = map(int,input().split())
if n%m!=0:
    print(-1)
else:
    temp = n//m
    ans = 0
    while temp%3==0:
        ans+=1
        temp//=3
    while temp%2==0:
        ans+=1
        temp//=2
    if temp==1:
        print(ans)
    else:
        print(-1)