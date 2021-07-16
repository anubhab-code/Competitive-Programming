for _ in range(int(input())):
    n,k = map(int,input().split())
    l1,l2 = [],[]
    for i in range(1,k-(n-k)):
        l1.append(i)
    for j in range(k-(n-k),k+1):
        l2.append(j)
    ans= l1+l2[::-1]
    print(*ans)