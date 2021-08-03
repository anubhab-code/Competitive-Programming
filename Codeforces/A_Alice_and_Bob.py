from math import gcd
n = int(input())
g=0
l=list(map(int,input().split()))
for i in l:
    g=gcd(g,i)
ma=max(l)
if (ma//g - n)%2==0:
    print('Bob')
else:
    print('Alice')