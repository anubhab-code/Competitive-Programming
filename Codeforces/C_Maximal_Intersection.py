n=int(input())
l,r,a=[],[],[]
for _ in range(n):
	u,v=map(int,input().split())
	l.append(u)
	r.append(v)
	a.append((u,v))
l=sorted(l)
r=sorted(r)
ans=0
for i in a:
	u=i[0]
	v=i[1]
	ml=0
	mr=0
	if u!=l[-1]:
		ml=l[-1]
	else:
		ml=l[-2]
	if v!=r[0]:
		mr=r[0]
	else:
		mr=r[1]
	ans=max(ans,mr-ml)
print(ans)