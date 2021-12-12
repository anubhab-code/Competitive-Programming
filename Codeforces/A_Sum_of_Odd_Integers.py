for _ in range(int(input())):
    n,k = map(int,input().split())
    if k**2<=n:
        if (n+k)%2==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")