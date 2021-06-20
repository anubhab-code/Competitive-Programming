n,k = map(int, input().split())
h = list(map(int,input().split()))
m = sum(h[:k])
p = sum(h[:k])
ans = 1
for i in range(k,n):
    p += h[i]-h[i-k]
    if p < m:
    	ans = i-k+2
    	m = p
print(ans)