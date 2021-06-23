mod = int(1e9 + 7)
for _ in range(int(input())):
    x,y = map(int,input().split())
    n = int(input())
    n -= 1
    z = y-x
    if n % 3 == 0:
        if n % 2 == 0:
            print(x % mod)
        else:
            print(-x % mod)
    elif n % 3 == 1:
        if n % 2 == 1:
            print(y % mod)
        else:
            print(-y % mod)
    elif n % 3 == 2:
        if n % 2 == 0:
            print(z % mod)
        else:
            print(-z % mod)