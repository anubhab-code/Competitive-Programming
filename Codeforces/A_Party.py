n = int(input())
l = []
for i in range(n):
    temp=int(input())
    l.append(temp)
ans = 0
for i in range(n):
	t1=0
	while i>=0:
		t1+=1
		i=l[i]-1
	ans=max(ans,t1)
print(ans)