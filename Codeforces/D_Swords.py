import math
for _ in range(1):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    mx=max(l)
    sum1=mx-l[0]
    gc=mx-l[0]
    for i in range(1,n):
        if mx-l[i]>0:
            sum1+=(mx-l[i])
            gc=math.gcd(gc,mx-l[i])
    print(sum1//gc,gc)