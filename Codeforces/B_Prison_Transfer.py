n,t,c = map(int,input().split())
l = list(map(int,input().split()))
x = 0
y = 0
z = 0
for i in range(n):
    if l[i] > t:
        z=i+1
        if y-c+1 >0:
            x+=y-c+1
        y=0
    else:
        y+=1
if n-z-c+1 > 0:
    x += n-z-c+1
if x < 0:
    print(0)
else:
    print(x)