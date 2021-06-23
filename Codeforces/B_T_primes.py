import math
t = int(input())
arr = input().split()
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for n in arr:
    n = int(n)
    sqrt = int(math.sqrt(n))
    if n==sqrt*sqrt and n!=1 and isprime(sqrt):
        print("YES")
    else:
        print("NO")