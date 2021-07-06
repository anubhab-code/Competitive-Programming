n,m = list(map(int,input().split()))
cost = list(map(int,input().split()))
ans=0
for i in range(m):
	f,s = list(map(int,input().split()))
	ans += min(cost[f-1],cost[s-1])
print(ans)