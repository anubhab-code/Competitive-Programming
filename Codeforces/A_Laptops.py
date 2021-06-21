q=0
for i in range(int(input())):
	n=list(map(int,input().split()))
	q+=(n[0]!=n[1])
if q>1:
	print('Happy Alex')
else:
	print('Poor Alex')