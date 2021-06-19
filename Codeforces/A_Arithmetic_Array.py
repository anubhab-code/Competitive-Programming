for _ in range(int(input())):
    n=int(input())
    check=sum(list(map(int,input().split())))
    if check==n:
        print(0)
    elif check<n:
        print(1)
    else:
        print(check-n)