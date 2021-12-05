for _ in range(int(input())):
    x,n=map(int,input().split())
    ans=0
    if n%4==1:
        ans=-n
    if n%4==2:
        ans=1
    if n%4==3:
        ans=n+1
    if n%4==0:
        ans=0
    if abs(x)%2==1:
        ans=-ans
    print(ans+x)