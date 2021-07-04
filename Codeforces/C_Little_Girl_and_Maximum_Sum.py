n,q = map(int,input().split())
l = list(map(int,input().split()))
cur = [0]*(n+1)
x = []
ans = 0
for i in range(q):
    a, b = map(int,input().split())
    cur[a] += 1
    if b+1 <= n:
        cur[b+1] -= 1
    x.append((a, b))
l = sorted(l)
for i in range(1,n+1):
    cur[i] += cur[i-1]
cur=sorted(cur)
ans = 0
while l:
    ele = l.pop()
    no = cur.pop()
    ans += no*ele
print(ans)