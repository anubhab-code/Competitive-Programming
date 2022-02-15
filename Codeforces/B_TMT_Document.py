for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    check = 0
    for i in s:
        if i == "T":
            c += 1
        else:
            c -= 1
        check = n//3
        if c>check or c<0:
            break
    if c == check:
        print("YES")
    else:
        print("NO")