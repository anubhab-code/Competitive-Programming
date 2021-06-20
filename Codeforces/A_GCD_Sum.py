import math
for _ in range(int(input())):
    n=int(input())
    while True:
        a=0
        for i in str(n):
            a+=int(i)
        if math.gcd(a,n)>1:
            print(n)
            break
        n+=1
    