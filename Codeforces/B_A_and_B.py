for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    while 1:
        temp=(ans*(ans+1))//2
        diff=temp-abs(a-b)
        if diff>=0 and diff%2==0:
            print(ans)
            break
        ans+=1