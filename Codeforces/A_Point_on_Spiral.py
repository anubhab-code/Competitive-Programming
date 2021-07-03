x,y=map(int,input().split())
if x==0 and y==0:
    print(0)
elif y<x and y<=1-x:
    print(-4*y)
elif y>1-x and y<=x:
    print(4*(x-1)+1)
elif y>x and y>=-x:
    print(4*(y-1)+2)
else:
    print(4*(-x-1)+3)