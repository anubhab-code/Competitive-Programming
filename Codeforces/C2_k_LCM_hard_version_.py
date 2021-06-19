for _ in range(int(input())):
    n,k=map(int,input().split())
    n=n-k+3
    if n%4==0:
        print((n//2)//2,(n//2)//2,n//2,end=" ")
    elif n%4==1:
        print(n//2,n//2,1,end=" ")
    elif n%4==2:
        print((n//2)-1,(n//2)-1,2,end=" ")
    else:
        print(n//2,n//2,1,end=" ")
    print("1 "*(k-3))