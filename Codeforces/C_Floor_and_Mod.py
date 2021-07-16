for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    for i in range(1,int(a**0.5)+2):
        ans+=max(min(b,a//i-1)-i,0)
    print(ans)