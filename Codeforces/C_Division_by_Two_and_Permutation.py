from collections import defaultdict 
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l = sorted(l)
    ans = []
    check = defaultdict(int)
    for j in range(len(l)):
        temp=bin(l[j])[2:]
        ans.append(temp)
    flag = 1
    for i in range(n,0,-1):
        t2 = bin(i)[2:]
        f2 = 0
        for x in range(n):
            if ans[x].startswith(t2):
                if check[x]:
                    pass
                else:
                    check[x] = 1
                    f2 = 1
                    break
        if f2:
            pass
        else:
            print("NO")
            flag = 0
            break
    if flag:
        print("YES")