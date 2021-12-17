for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    p  = "x"
    ans = ""
    for i in s:
        if i[0]==p:
            ans+=i[1]
        else:
            ans+=i
        p = i[1]
    final="b"*(n-len(ans))+ans
    print(final)
        