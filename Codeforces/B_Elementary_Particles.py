from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    check = defaultdict(list)
    for i in range(n):
        check[l[i]].append(i)
    ans = 0
    flag = 0
    for i in check.keys():
        if not len(check[i])>=2:
            pass
        if len(check[i])>=2:
            flag = 1
            for j in range(len(check[i])-1):
                t2 = check[i][j]+n-check[i][j+1]
                ans = max(ans,t2)
    if not flag:
        print(-1)
    else:
        print(ans)