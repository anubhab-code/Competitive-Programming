from math import gcd
x,y,a,b = map(int,input().split())
check = (x*y)//gcd(x,y)
ans = (b//check)-(a//check)
if a%check==0:
    ans+=1
print(ans)