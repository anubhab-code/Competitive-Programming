for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%4==0:
        print((n//2)//2,(n//2)//2,n//2)
    elif n%4==1:
        print(n//2,n//2,1)
    elif n%4==2:
        print((n//2)-1,(n//2)-1,2)
    else:
        print(n//2,n//2,1)