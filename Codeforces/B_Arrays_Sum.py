import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    dif = len(set(l))
    if k>=dif:
        print(1)
    elif k==1:
        print(-1)
    else:
        ans = 0
        while dif>0:
            ans+=1
            dif-=k
            if dif!=0:
                dif+=1
        print(ans)