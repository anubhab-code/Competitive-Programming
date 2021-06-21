n = int(input())
l = list(map(int,input().split()))
maxm = 0
minm = len(l)-1
for i in range(len(l)):
	if l[i]> l[maxm]:
		maxm=i
	if l[i]<=l[minm]:
		minm = i
if minm>maxm:
	print (n+maxm-minm-1)
else:
	print (n+maxm-minm-2)