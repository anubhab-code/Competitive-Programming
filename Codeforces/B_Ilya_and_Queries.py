s = input()
m = int(input())
memo = [0]*len(s)
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        memo[i] = memo[i-1] + 1
    else:
        memo[i] = memo[i-1]
for i in range(m):
	l,r = map(int,input().split())
	print(memo[r-1] - memo[l-1])