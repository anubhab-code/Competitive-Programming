def f(x):
	return str(bin(x)).count('1')
n = int(input())
a = list(map(int, input().split()))
ans = [f(x) for x in a]
s = set(ans)
counts = {x:ans.count(x) for x in s}
ans = 0
for i in counts:
	ans += (counts[i]*(counts[i]-1))//2
print(ans)