for _ in range(int(input())):
    a = list(map(int,input().split()))
    ans = 0
    for x in a:
        if x > a[0]:
            ans += 1
    print(ans)