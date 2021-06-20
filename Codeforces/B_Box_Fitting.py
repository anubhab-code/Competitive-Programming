from typing import Counter
for _ in range(int(input())):
    n,w=map(int,input().split())
    width=list(map(int,input().split()))
    width=sorted(width)[::-1]
    d=Counter(width)
    ans=0
    lsum=0
    while n:
        for j in d:
            while d[j]>0 and lsum+j<=w:
                d[j]-=1
                lsum+=j
                n-=1
        lsum=0
        ans+=1
    print(ans)