for _ in range(int(input())):
    a,b = map(int,input().split())
    ans = ""
    while a and b:
        ans += '1'
        ans += '0'
        a -= 1
        b -= 1
    if a:
        ans += a*'0'
    if b:
        ans += b*'1'
    print(ans)