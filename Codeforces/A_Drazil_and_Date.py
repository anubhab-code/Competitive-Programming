a,b,s=map(int,input().split())
a=abs(a)
b=abs(b)
if a==0 and b==0:
    if s%2==0:
        print("Yes")
    else:
        print("No")
elif s<(a+b):
    print("No")
elif (a+b)%2==0:
    if s%2==0:
        print("Yes")
    else:
        print("No")
elif (a+b)%2!=0:
    if s%2!=0:
        print("Yes")
    else:
        print("No")