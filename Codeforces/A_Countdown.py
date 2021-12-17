for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input()))
    ans=sum(a)
    check=0
    for i in a:
        if i==0:
            pass
        else:
            check+=1
    ans+=check
    if a[-1]!=0:
        ans-=1
    print(ans)