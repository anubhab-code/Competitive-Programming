a,b,c = map(int,input().split())
x,y,z = 0,0,0
s = a+b+c
if s%2==0:
    x = (a+b-c)//2
    y = (b+c-a)//2
    z = (a+c-b)//2
    if x>=0 and y>=0 and z>=0:
        print(x,y,z)
    else:
        print("Impossible")
else:
    print("Impossible")