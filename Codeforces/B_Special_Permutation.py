for _ in range(int(input())):
    n,a,b=map(int,input().split())
    l,r=[a],[b]
    if a<b:
        for i in range(b+1,n+1):
            l.append(i)
        for i in range(1,a):
            r.append(i)
        if len(l)>n//2 or len(r)>n//2:
            print(-1)
            continue
        cur=a+1
        while len(l)!=n//2:
            l.append(cur)
            cur+=1
        while len(r)!=n//2:
            r.append(cur)
            cur+=1
        if len(l)>n//2 or len(r)>n//2:
            print(-1)
            continue
        print(*(l+r))
    else:
        if a==n//2 +1 and b==n//2:
            for i in range(n,0,-1):
                print(i, end=" ")
            print()
        else:
            print(-1)