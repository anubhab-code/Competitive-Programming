mod=10**9+7
for _ in range(int(input())):
    n,k=map(int,input().split())
    cnt=0
    ans=0
    while k:
        if k&1:
            ans=(ans+pow(n,cnt,mod))%mod
        cnt+=1
        k//=2
    print(ans)