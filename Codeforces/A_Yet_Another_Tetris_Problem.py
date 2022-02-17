for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    temp = min(l)
    flag = 1
    for i in range(n):
        if (l[i]-temp)%2==1:
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")