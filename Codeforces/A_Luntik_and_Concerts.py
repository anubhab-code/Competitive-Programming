for _ in range(int(input())):
    a,b,c=map(int,input().split())
    ans=a+2*b+3*c
    if ans%2==0:
        print(0)
    else:
        print(1)