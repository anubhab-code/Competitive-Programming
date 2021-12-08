for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    temp=[-1]*n
    ans=1
    for i in range(n):
        if ans:
            t=i+2
            while t>=2:
                tt=t
                t-=1
                if l[i]%tt!=0:
                    temp[i]=tt-1
                    break
            if temp[i]==-1:
                ans=0
    if ans:
        print("YES")
    else:
        print("NO")