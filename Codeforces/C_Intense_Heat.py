n, k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(1,n):
	a[i] += a[i-1]
a = [0] + a[:]
ans = 0
for i in range(k, n+1):
	m = 0
	for j in range(1,n-i+2):
		m = max(m, a[j+i-1]-a[j-1])
	ans = max(ans, m/i)
print(ans)