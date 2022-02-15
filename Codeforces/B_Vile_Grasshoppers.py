p,y = map(int,input().split())
ans = -1
while y>p:
	flag,i=1,2
	while i<=p and i**2<=y:
		if y%i==0:
			flag=0
			break
		i+=1
	if flag:
		ans=y
		break
	y-=1
print(ans)