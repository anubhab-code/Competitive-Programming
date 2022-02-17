for _ in range(int(input())):
    x,n,m=map(int,input().split())
    while n and x > (x//2)+10:
        x = (x//2)+10
        n -= 1
    if x <= m * 10:
        print("YES")
    else:
        print("NO")