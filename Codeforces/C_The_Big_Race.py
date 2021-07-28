import math
t,w,b = map(int,input().split())
l = t//(w*b//math.gcd(w,b))
n = l*min(w,b) + min(t-l*(w*b//math.gcd(w,b))+1,min(w,b)) - 1
print(n//math.gcd(n,t),'/',t//math.gcd(n,t),sep='')