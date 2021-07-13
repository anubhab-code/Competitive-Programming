def fun(n): 
    fact = 1 
    for i in range(1,n+1):
        fact = fact * i
    return fact
n= int(input())
k = fun(n)
j = fun(n//2)
l = j//(n//2)
print(((k//(j**2))*(l**2))//2)