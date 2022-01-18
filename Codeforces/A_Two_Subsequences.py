for _ in range(int(input())):
    n = input()
    m = min(n)
    ans = n.replace(m,"",1)
    print(m,ans)