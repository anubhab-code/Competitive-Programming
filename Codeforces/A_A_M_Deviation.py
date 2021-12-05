for _ in range(int(input())):
    a,b,c=map(int,input().split())
    ans=a+c-b-b
    ans=abs(ans)
    c1=ans%3
    c2=ans%(-3)
    c2=abs(c2)
    if c1<c2:
        print(c1)
    else:
        print(c2)