for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    check = sum(l)
    if check==0:
        print("NO")
    else:
        print("YES")
        l = sorted(l)
        if check>0:
            print(*(l[::-1]))
        else:
            print(*l)
