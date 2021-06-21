import math
for _ in range(int(input())):
    final=[]
    a,b,c,d=map(int,input().split())
    if b>=a:
        final.append(b)
    elif d>=c:
        final.append(-1)
    else:
        x,y=a-b,c-d
        z=math.ceil(float(x)/float(y))
        final.append((z*c)+b)
    print(int(*final))