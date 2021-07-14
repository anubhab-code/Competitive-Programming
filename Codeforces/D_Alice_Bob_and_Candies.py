for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	a,b=0,0
	i=0
	j=n-1
	left=0
	right=0
	count=0
	while i<=j:
		if left==0:
			while left<=right and i<=j:
				left+=arr[i]
				i+=1
			a+=left
			right=0
		elif right==0:
			while right<=left and i <=j:
				right+=arr[j]
				j-=1
			b+=right
			left=0
		count+=1
	print(count,a,b)