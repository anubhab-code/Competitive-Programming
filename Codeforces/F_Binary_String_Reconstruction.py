for _ in range(int(input())):
    n0,n1,n2=map(int,input().split())
    n=n0+n1+n2+1
    ans=""
    if n1==0:
        if n2==0:
            for i in range(n0+1):
                ans+="0"
        else:
            for i in range(n2+1):
                ans+="1"
    else:
        for i in range(n2+1):
            ans+="1"
        for i in range(n0+1):
            ans+="0"
        for i in range(1,n1):
            if i%2==1:
                ans+="1"
            else:
                ans+="0"
    print(ans)