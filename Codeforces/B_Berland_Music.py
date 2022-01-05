from collections import defaultdict
for _ in range(int(input())):
    a = defaultdict(int)
    b = defaultdict(int)
    check = defaultdict(int)
    n = int(input())
    l = list(map(int,input().split()))
    s = input()
    for i in range(n):
        check[l[i]] = i
        if s[i]!="1":
            a[l[i]] = 1
        else:
            b[l[i]] = 1
    temp = 1
    for i in range(1,n+1):
        if a[i]:
            l[check[i]] = temp
            temp+=1
    for i in range(1,n+1):
        if b[i]:
            l[check[i]] = temp
            temp+=1
    ans=l
    print(*ans)