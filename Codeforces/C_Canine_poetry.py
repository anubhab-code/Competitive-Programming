for _ in range(int(input())):
    s=list(input())
    s = ["$","$"]+s
    n = len(s)
    ans = 0
    for i in range(2,n):
        if s[i] == s[i-1] or s[i] == s[i-2]:
            s[i] = '@'
            ans += 1
    print(ans)