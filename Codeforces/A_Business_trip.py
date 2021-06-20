def fun(k,l):
	if k==0:
		return 0 
	for i in range(12):
		if sum(l[:i+1])>=k:
			return i+1
	return -1

k=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
print(fun(k,l))