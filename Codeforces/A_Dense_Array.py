for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 0
    temp = l[0]
    for i in range(1,n):
        t1 = l[i]
        t2,t3 = min(temp,t1),max(temp,t1)
        while t3>2*t2:
            ans+=1
            t2*=2
        temp = t1
    print(ans)
    