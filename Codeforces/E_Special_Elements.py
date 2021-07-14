for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    pre=[0]
    for i in range(n):
        pre.append(l[i]+pre[-1])
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    c=0
    for i in range(n):
        for j in range(i+1,n):
            s=pre[j+1]-pre[i]
            if s in d and d[s]!=0:
                c+=d[s]
                d[s]=0
    print(c)