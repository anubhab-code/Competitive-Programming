from math import sqrt
n = 10**6
l = [-1]*(n+1)
mod = 1073741824

def hehe(f):
	count=0
	for i in range(1,int(sqrt(f))+1):
		if f%i==0:
			if f/i==i:
				count+=1
			else:
				count+=2
	return count
	
a,b,c = map(int,input().split())
ans = 0
for i in range(1,a+1):
	for j in range(1,b+1):
		for k in range(1,c+1):
			if l[i*j*k]==-1:	
				l[i*j*k]=hehe(i*j*k)
			ans += l[i*j*k]%mod
ans %= mod
print(ans)