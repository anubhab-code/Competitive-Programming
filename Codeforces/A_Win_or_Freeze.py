import math

def primeFactors(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            a.append(i)
            n = n // i
    if n > 2:
        a.append(n)
    return a

n = int(input())
a = primeFactors(n)
if len(a) == 0 or len(a)==1:
    print(1)
    print(0)
elif len(a) == 2 and a[0] * a[1] == n:
    print(2)
else:
    print(1)
    print(a[0] * a[1])