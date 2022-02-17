for _ in range(int(input())):
    n = int(input())
    s = input()
    r,b = [],[]
    for i in s[0::2]:
        r.append(int(i))
    for j in s[1::2]:
        b.append(int(j))
    if n%2==1:
        ans = 2
        for i in r:
            if i%2==1:
                ans = 1
                break
        print(ans)
    else:
        ans = 1
        for i in b:
            if i%2==0:
                ans = 2
                break
        print(ans)