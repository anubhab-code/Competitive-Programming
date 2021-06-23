n, m = map(int, input().split())
l = list(map(int, input().split()))
l = l[::-1]
s = set()
ans= []
for i in range(n):
    s.add(l[i])
    ans.append(len(s))
for j in range(m):
    c = int(input())
    print(ans[n-c])