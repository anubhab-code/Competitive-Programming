for _ in range(int(input())):
    n,k=map(int, input().split())
    temp=2
    while n%temp!=0:
        temp+=1
    ans=n+temp+(k-1)*2
    print(ans)