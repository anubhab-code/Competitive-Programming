n=int(input())
if n==1 or n==2:
    print(-1)
elif n%2==1:
    print(((n**2)+1)//2,((n**2)-1)//2)
else:
    a=(n**2)//2
    b=2
    print((a+b)//2,(a-b)//2)