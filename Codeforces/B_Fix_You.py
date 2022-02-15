for _ in range(int(input())):
	n,m = map(int,input().split())
	ans = 0
	temp = []
	for i in range(n):
		t1 = list(input())
		temp.append(t1)
	for i in range(n):
		for j in range(m):
			p = temp[i][j]
			if p=="C":
				continue
			if i==n-1 and p=="D":
				ans+=1
			if j==m-1 and p=="R":
				ans+=1
	print(ans)