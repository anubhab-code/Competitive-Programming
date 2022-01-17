for _ in range(int(input())):
    n = int(input())
    s = input()
    alpha = set(s)
    ans = n
    countImpossible = 0
    for i in alpha:
        curr = 0
        lb, ub = 0, n - 1
        while lb < ub:
            if s[lb] == s[ub]:
                lb += 1
                ub -= 1
                continue
            else:
                if s[lb] == i:
                    lb += 1
                    curr += 1
                    continue
                elif s[ub] == i:
                    ub -= 1
                    curr += 1
                    continue
                else:
                    curr = n + 1
                    lb += 1
                    ub -= 1
                    continue
        dup = s
        dup = dup.replace(i, '')
        if dup != dup[::-1]:
            countImpossible += 1
        ans = min(ans, curr)
    if countImpossible == len(alpha):
        ans = -1
    print(ans)