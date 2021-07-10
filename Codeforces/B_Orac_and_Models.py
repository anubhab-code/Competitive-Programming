import math 
for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	ans=[1]*n
	for i in range(n):
		mx=0
		for j in range(1,int(math.sqrt(i+1))+1):
			if (i+1)%j==0:
				if l[i]>l[j-1] :
					mx=max(mx,ans[j-1])
				if l[i]>l[((i+1)//j)-1]:
					mx=max(mx,ans[(i+1)//j-1])
		ans[i]+=mx
	print(max(ans))