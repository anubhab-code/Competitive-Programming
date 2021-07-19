import math
for _ in range(int(input())):
    k,n,a,b=map(int,input().split())
    div=k//a
    rem=k%a
    if k//b<n:
        print(-1)
        continue
    if k//b==n:
        if k%b==0:
            print(-1)
            continue
    if div<n:
        y=math.ceil((k-a*n-1)/(b-a))
        print(n-y)
    elif div==n:
        if rem:
            print(n)
        else:
            print(n-1)
    else:
        print(n)