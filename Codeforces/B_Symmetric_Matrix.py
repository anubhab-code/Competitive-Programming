for _ in range(int(input())):
    n,m = map(int,input().split())
    flag = 0
    for i in range(n):
        a,b = map(int,input().split())
        c,d = map(int,input().split())
        if b==c:
            flag = 1
    if m%2==0 and flag:
        print("YES")
    else:
        print("NO")
