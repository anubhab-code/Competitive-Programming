import math
for _ in range(int(input().strip())):
    n=int(input())
    x=[]
    y=[]
    for i in range(2*n):
        a,b = map(int,input().split())
        if a==0:
            if b<0:
                b=-b
            y.append(b)
        else:
            if a<0:
                a=-a
            x.append(a)
    x=sorted(x)
    y=sorted(y)
    ans=0
    for i in range(n):
        ans+=math.sqrt(x[i]*x[i]+y[i]*y[i])
    print(ans)