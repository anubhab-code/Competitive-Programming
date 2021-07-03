def prime(n):
    if n<4:
        return (n==2 or n==3)
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(n**0.5)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

n = int(input())
if prime(n):
    print(1)
    print(n)
elif prime(n-2):
    print(2)
    print(2,n-2)
else:
    print(3)
    c=n-3
    for i in range(3,n,2):
        if prime(i) and prime(c-i):
            print(3,i,c-i)