for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	i=1
	rng=1
	while rng<k:
		i+=1
		rng+=i
	pos=n-i-1
	next_a=rng-k
	st='a'*n
	print("a"*(pos)+"b"+"a"*(next_a)+"b"+"a"*(n-(pos+next_a)-2))