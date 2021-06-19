for _ in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    ans=[]
    h=sorted(h)
    a,b=h[1]-h[0],h[n-1]-h[n-2]
    d=min(a,b)
    c=-1
    for i in range(1,n-1):
        if h[i+1]-h[i]<d:
            c=i
            d=h[i+1]-h[i]
    if c!=-1:
        ans.append(h[c])
        for i in range(c+2,n):
            ans.append(h[i])
        for i in range(0,c):
            ans.append(h[i])
        ans.append(h[c+1])
        
    else:
        if a<b:
            ans.append(h[0])
            for i in range(2,n):
                ans.append(h[i])
            ans.append(h[1])
        else:
            ans.append(h[n-2])
            for i in range(n):
                if i!=n-2:
                    ans.append(h[i])
    print(*ans)
            