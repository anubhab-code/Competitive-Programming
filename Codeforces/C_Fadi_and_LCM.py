import math 
n=int(input())
for i in range(int(n**0.5),0,-1):
	if n%i==0 and math.gcd(i,n//i)==1:
		ans=i
		break
print(ans,n//ans)