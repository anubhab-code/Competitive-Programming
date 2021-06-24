import math
r,x,y,x1,y1=map(int,input().split())
d=((x-x1)**2+(y-y1)**2)**0.5
print(math.ceil(d/(2*r))) 