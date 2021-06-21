x=int(input())
y=int(input())
z=int(input())
if x==1 and z==1:
    print(y+2)
elif x==1:
    print(z*(x+y))
elif y==1:
    print(max(x*(y+z),z*(x+y)))
elif z==1:
    print(x*(y+z))
else:
    print(x*y*z)