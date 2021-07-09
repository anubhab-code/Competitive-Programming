for _ in range(int(input())):
	n,k = list(map(int,input().split()))
	ans = float('inf')
	for i in range(int(n**0.5+1),0,-1):
		if n%i==0 and i<=k:
			if n/i<=k :				
				ans=min(ans,i)
			elif i<=k :
				ans=min(ans,n//i)
	print(ans)