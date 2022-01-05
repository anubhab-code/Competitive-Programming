for _ in range(int(input())):
	n,k= map(int,input().split())
	s=1
	ans=0
	while s<k:
		s*=2
		ans+=1
	t=max(0,(n-s))//k
	s+=t*k
	if s<n:
		ans+=1
	print(ans+t)