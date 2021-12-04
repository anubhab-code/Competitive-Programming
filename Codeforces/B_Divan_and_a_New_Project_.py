for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        ans.append([a[i],i+1])
    ans.sort()
    res = [0]*(n+1)
    temp = 0
    check = 1
    for i in range(n-1,-1,-2):
        a = ans[i]
        if i-1<0:
            pass
        else:
            b = ans[i-1]
            temp += 2*check*(a[0]+b[0])
            res[a[1]] = check
            res[b[1]] = -check
            check+=1
    if n%2==0:
        pass
    else:
        b = ans[0]
        temp += 2*check*(b[0])
        res[b[1]] = check
    print(temp)
    print(*res)