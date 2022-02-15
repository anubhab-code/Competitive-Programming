for _ in range(int(input())):
    n = input()
    ans = 10*(int(n[0])-1)
    ans += ((len(n)+1)*(len(n)))//2
    print(ans)