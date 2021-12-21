from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    check = defaultdict(int)
    l2 = []
    for i in range(n):
        if not (l[i]>=1 and l[i]<=n and not check[l[i]]):
            l2.append(l[i])
        else:
            check[l[i]] = 1
    l2=sorted(l2)
    l3 = [0]*(n+1)
    for j in check.keys():
        l3[j] = 1
    ans=0
    flag = 1
    for i in range(1,n+1):
        if not l3[i]:
            if not (i <= (l2[ans]//2 - (l2[ans]%2==0))):
                flag = 0
                break
            else:
                ans+=1
                l3[i]=1
    if not flag:
        print(-1)
    else:
        print(len(l2))
        