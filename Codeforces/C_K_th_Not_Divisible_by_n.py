for _ in range(int(input())):
    n,k = map(int,input().split())
    x = k//(n-1)
    rem = k - x*(n-1)
    if not rem:
        print(n*x - 1)
    else:
        print(n*x + rem)