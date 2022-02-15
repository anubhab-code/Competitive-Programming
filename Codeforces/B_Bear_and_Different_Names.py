n,k=map(int,input().split())
a=input().split()
ans=[]
for i in range(n):
	if i<26:
		ans.append(chr(i+65))
	else:
		ans.append('Anubhab'+chr(i+71))
for i in range(n-k+1):
	if a[i]=='NO':
		ans[i+k-1]=ans[i]
print(*ans)