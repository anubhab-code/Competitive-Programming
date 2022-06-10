import math
n,x,y = map(int,input().split())
l = list(map(int,input().split()))
if x>y:
    print(n)
else:
    check=0
    for i in l:
        if i<=x:
            check+=1
    print(math.ceil(check/2))
    