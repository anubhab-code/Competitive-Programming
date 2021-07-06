for _ in range(int(input())):
	n,k = map(int,input().split())
	l = list(map(int,input().split()))
	m=(n//2)+1	
	ans=0
	for i in range(1,k+1):
		ans+=l[-m*i]
	print(ans)