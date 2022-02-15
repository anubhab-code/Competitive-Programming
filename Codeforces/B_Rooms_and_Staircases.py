for _ in range(int(input())):
    n = int(input())
    s = input()
    if "1" not in s:
        print(n)
    else:
        i = s.index("1")
        j = s[::-1].index("1")
        print(max(2*(i+1),2*(n-i),2*(j+1),2*(n-j)))