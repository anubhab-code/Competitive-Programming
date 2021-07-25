import math
a,b,c,d = list(map(int,input().split()))
if b >= c*d:
    print(-1)
else:
    print(math.ceil(a/(c*d-b)))