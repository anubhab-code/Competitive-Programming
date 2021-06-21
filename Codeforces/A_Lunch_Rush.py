n,k=map(int,input().split())
maxm=-float('inf')
for i in range(n):
	f,t=map(int,input().split())
	if t<=k:
		maxm=max(maxm,f)
	else:
		maxm=max(maxm,f-(t-k))
print(maxm)