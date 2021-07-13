for _ in range(int(input())):
    s = input()
    cur, mn, ans = 0, 0, len(s)
    for i in range(len(s)):
        cur += 1 if s[i] == '+' else -1
        if cur < mn:
            mn = cur
            ans += i+1
    print(ans)