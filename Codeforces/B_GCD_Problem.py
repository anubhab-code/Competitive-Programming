from math import gcd
for _ in range(int(input())):
    n = int(input())
    if (n-1)%2!=1:
        n-=1
        i = int(n/2)
        while i >= 1:
            if gcd(i,n-i)==1:
                print(i,n-i,1)
                break
            i-=1
    else:
        print(2,(n-3),1)