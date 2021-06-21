n=int(input())
l=list(map(int,input().split()))
i=n-1
while True:
	l.sort()
	if l[i]>l[0]:
		l[i]-=l[0]
		i-=1
	else:
		if l[0]==l[n-1]:
			break
		i=n-1
		continue
print(sum(l))