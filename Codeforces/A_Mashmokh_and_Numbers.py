n,k=map(int,input().split())
if k<n//2 or (n==1 and k!=0):
	print(-1)
else:
	if n==1:
		print(1)
	else:
		x=r=k-(n-2)//2
		while r<=x+n:
			r+=x
		ans=[r,x]
		for i in range(2,n):
			ans.append(ans[1]+i-1)
		print(*ans)