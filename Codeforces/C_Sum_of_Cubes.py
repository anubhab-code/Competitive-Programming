d = {}
m = int(1e4)+1
for i in range(1,m):
    d[i**3] = 1
for _ in range(int(input())):
    n = int(input())
    flag = 0
    for i in range(1,m):
        temp = i**3
        if n-temp in d:
            flag = 1
            break
    if flag:
        print("YES")
    else:
        print("NO")