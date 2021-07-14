for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%2==0:
        if k%n==0:
            print(n)
        else:
            print(k%n)
    else:
        if k<=n//2:
            print(k)
        else:
            bnew=k+((k-1)//(n//2))
            if bnew%n==0:
                print(n)
            else:
                print(bnew%n)