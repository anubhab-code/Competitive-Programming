for _ in range(int(input())):
	n,m,a,b=list(map(int,input().split()))
	if sum((n,m))<sum((a,b)):
		print('no')
		continue
	elif min(n,m)<b:
		print('no')
		continue
	else:
		print('yes')