from math import sqrt
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=int(input())
ans=[]
for i in range(2,n+1):
    if isPrime(i):
        j=i
        while j<=n:
            ans.append(j)
            j*=i
print(len(ans))
print(*ans)