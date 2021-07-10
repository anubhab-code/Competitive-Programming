from math import gcd 
a,b = map(int,input().split())
k = set(map(int,input().split()[1::]))
k1 = set(map(int,input().split()[1::]))
n=((a*b)//gcd(a,b))*max(a,b)
for i in range(n+1):
    if i%a in k or i%b in k1:
        k.add(i%a)
        k1.add(i%b)
if len(k)==a and len(k1)==b:
    print("Yes")
else:
    print("No")