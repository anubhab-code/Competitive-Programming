for _ in range(int(input())):
    a,b,c=map(int,input().split())
    ma=max(max(a,b),c)
    check=2*abs(b-a)
    if check<ma:
        print(-1)
    else:
        ans=(c+check//2)%check
        if ans==0:
            ans=check
        print(ans)