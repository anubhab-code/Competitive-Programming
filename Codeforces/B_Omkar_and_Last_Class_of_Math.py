for _ in range(int(input())):
	n=int(input())
	if n%2==0:
		print(n//2,n//2)
		continue
	mn_i,mn_j=1,n-1
	for i in range(1,int(n**0.5+2)):
		if n/(1+i)==n//(1+i):
			a=n//(1+i)
			b=n-a
			mn_i=a
			mn_j=b
			break
	print(mn_i,mn_j)