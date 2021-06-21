for _ in range(int(input())):
    n,x,t=map(int,input().split())
    check=min(t//x,n-1)
    ans=max(0,check*(check-1)//2)
    final=ans+(check*(n-check))
    if check==0:
        print(0)
    else:
        print(final)