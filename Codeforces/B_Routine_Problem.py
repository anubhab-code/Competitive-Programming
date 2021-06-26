import math
a,b,c,d = map(int,input().split())
if a/b<c/d:
    nu = b*c-a*d
    de = b*c
else:
    nu = d*a-b*c
    de = d*a
x=math.gcd(nu,de)
nu=nu//x
de=de//x
print(str(nu)+'/'+str(de))