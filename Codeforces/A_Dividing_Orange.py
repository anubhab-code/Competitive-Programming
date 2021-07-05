n,k = map(int,input().split())
l = list(map(int,input().split()))
l.append("fake")
idx=0
ans=[l[0]]
s=set(l)

for i in range(1,n*k+1):
	if i not in s:
		ans.append(i)
	if len(ans)==n:
		print(*ans)
		idx+=1
		ans=[l[idx]]