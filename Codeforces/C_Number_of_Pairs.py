for _ in range(int(input())):
    n,ll,r=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    target=r
    j=n-1
    ans=0
    for i in range(n):
        while(j>i and l[i]+l[j] > target):
            j-=1
        ans+=max(0,j-i)
    target=ll-1
    j=n-1
    ans1=0
    for i in range(n):
        while(j>i and l[i]+l[j] > target):
            j-=1
        ans1+=max(0,j-i)
    print(ans-ans1)