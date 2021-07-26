R,C,x,y,z,p=map(int,input().split())
x=x%4
y=y%2
z=z%4
for i in range(p):
    i,j=map(int,input().split())
    r,c=R,C
    for _ in range(x):
        i,j=j,r-i+1
        r,c=c,r
    for _ in range(y):
        i,j=i,c-j+1
    for _ in range(z):
        i,j=c-j+1,i
        r,c=c,r
    print(i,j)