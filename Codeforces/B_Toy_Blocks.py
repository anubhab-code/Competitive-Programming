for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    r = max(l)
    s = sum(l)
    if s%(n-1)==0:
        r=max(r,s//(n-1))
    else:
        r=max(r,s//(n-1)+1)
    print(r*(n-1)-s)