for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for x in a:
        if x not in d:
            d[x] = 0
        d[x] += 1
    ans,temp = 0,0
    for x in d:
        if d[x]%2 == 1:
            ans += 1
        else:
            temp += 1
    ans += (temp//2)*2
    print(ans)