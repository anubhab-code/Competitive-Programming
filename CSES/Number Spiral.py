for i in range(int(input())):
    n, m = map(int, input().split())
    if n > m:
        if n % 2:
            ans = (n-1)**2 + m
        else:
            ans = (n**2) - m + 1
    else:
        if m % 2:
            ans = (m**2) - n + 1
        else:
            ans = (m-1)**2 + n
    print(ans)