for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l=sorted(l)[::-1]
    c,t=0,0
    for i in range(k):
        if l[i]>=n:
            c+=1
        else:
            if t>=l[i]:
                break
            else:
                t+=n-l[i]
                c+=1
    print(c)