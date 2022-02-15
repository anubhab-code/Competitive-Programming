for _ in range(int(input())):
    s = input()
    n = len(s)
    check = s.count('1')
    if check<=1:
        print(0)
    else:
        temp = s[::-1]
        i = s.index('1')
        j = temp.index('1')
        ans = s[i:n-j]
        print(ans.count('0'))