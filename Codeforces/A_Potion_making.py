from math import gcd
for _ in range(int(input())):
    n=int(input())
    rem=gcd(n,100)
    print(100//rem)
    