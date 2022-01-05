from collections import defaultdict
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    t3=sum(l)
    l=sorted(l)
    t=[]
    for i in range(1,n):
        t.append(l[i]-l[0])
    c,mi=0,float('INF')
    while t and t3>k:
        t2=c+(t3-k+c)//(c+1)
        mi=min(mi,t2)
        t3-=t[-1]
        t.pop()
        c+=1
    if t3<=k:
        pass
    else:
        t4=(t3-k+c)//(c+1)
        c+=t4
    ans=min(mi,c)
    print(ans)
        