from heapq import *
q = int(input())
h,c=[],0
for i in range(q):
    q = list(map(int,input().split()))
    if q[0]==3:
        y=heappop(h)
        print(y+c)
    else:
        a, b = q
        if a == 1:
            heappush(h, b-c)
        else:
            c+=b