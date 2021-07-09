import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l = sorted(l)[::-1]
    j = 1
    idx = -1
    g = l[0]
    while j < n:
        temp = 0
        for i in range(j,n):
            y = math.gcd(g,l[i])
            if y > temp:
                temp = y
                idx = i
        l[j],l[idx] = l[idx],l[j]
        g = temp
        j+=1
    print(*l)