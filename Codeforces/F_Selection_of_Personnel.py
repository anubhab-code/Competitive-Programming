n=int(input())
a=n*(n-1)*(n-2)*(n-3)*(n-4)
b=a*(n-5)
c=b*(n-6)
a=a//120
b=b//720
c=c//5040
print(a+b+c)