for _ in range (int(input())) :
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    if k<=n:
        t,s = 0,0
        for i in range (k) :
            s += l[i]
        t = s
        for i in range (k,n) :
            s -= l[i-k]
            s += l[i]
            t = max(t,s)
        print(t + (k*(k-1))//2)
    else:
        s = sum(l)
        t1 = ((k*(k-1))//2) - ((k-n)*(k-n-1))//2
        print(t1+s) 