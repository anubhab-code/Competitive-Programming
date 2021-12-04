def hehe(n):
    res=1
    for i in range(n-1):
        res=(res*2)%1000000007
    return res


for _ in range(int(input())):
    n,m = map(int,input().split())
    l=[]
    ans=0
    for i in range(m):
        temp=list(map(int,input().split()))
        l.append(temp)
    for i in range(m):
        ans=ans|l[i][2]
    print((hehe(n)*ans)%1000000007)