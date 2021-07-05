n,m,k=list(map(int,input().split()))
matrix=[]
for i in range(n):
    l=list(map(str,input().split()))
    matrix.append(l)
row=[j for j in range(n)]
col=[j for j in range(m)]
 
ans=[]
for _ in range(k):
	s,x,y=input().split()
	x=int(x)-1
	y=int(y)-1
	if s=="c":
		col[x],col[y]=col[y],col[x]
	elif s=="r":
		row[x],row[y]=row[y],row[x]
	else:
		ans.append(matrix[row[x]][col[y]])
print("\n".join(ans))