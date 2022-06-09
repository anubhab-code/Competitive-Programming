for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    t1,t2={},{}
    check=1
    for i in range(n):
        t1[l[i]]=t1.get(l[i],[])+[i+1]
        t2[l[i]]=t2.get(l[i],[1,0])
        t2[l[i]][1]+=1
    for i in t2.keys():
        if t2[i][1]<2:
            check = 0
            break 
    if not check:
        print(-1)
    else:
        ans=[]
        for i in l:
            ans.append(t1[i][t2[i][0]%t2[i][1]])
            t2[i][0]+=1
        print(*ans)