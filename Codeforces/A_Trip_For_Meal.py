n=int(input())
a=int(input())
b=int(input())
c=int(input())
if n==1:
    print(0)
else:
    print(min(a,b)+(n-2)*min(a,min(b,c)))