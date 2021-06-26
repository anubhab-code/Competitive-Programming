n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
b = [0]*5
ans = []
for i in range(n):
    t = 0
    for j in range(m):
        if t < b[j]:
            t = b[j]
        t += a[i][j]
        b[j] = t
    ans.append(b[m-1])
print(*ans)