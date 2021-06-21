n,m=map(int,input().split())
final=set()
l={}
check=[0]*m
for i in range(n):
	l[i]=list(map(int,list(input())))
	for j in range(m):
		check[j]=max(l[i][j],check[j])
for i in l:
	for j in range(m):
		if check[j]==l[i][j]:
			final.add(i)
			break
print(len(final))