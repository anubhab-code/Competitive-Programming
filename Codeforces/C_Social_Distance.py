for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	st=input()
	ans=[]
	j=-10**7
	for i in range(n):
		if st[i]=='1':
			if i-j<=k:
				ans.pop()
			j=i
		elif st[i]=="0" and i-j>k:
			ans.append(i)
			j=i
	print(len(ans))