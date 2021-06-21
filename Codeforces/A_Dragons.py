s,n = map(int,input().split())
flag=1
l=[]
for i in range(n):
	a,b=map(int,input().split())
	l.append([a,b])
l = sorted(l)
for j in range(n):
	if s>l[j][0]:
		s+=l[j][1]
	else:
		flag=0	
		break
if flag==1:
	print("YES")
else:
	print("NO")