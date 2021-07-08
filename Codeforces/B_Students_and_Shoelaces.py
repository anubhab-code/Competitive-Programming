n, m = map(int, input().split())
g = {}
deg = [0]*(n+1)
for i in range(1, n+1):
    g[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]
    deg[a] += 1
    deg[b] += 1
    
ans = 0
for _ in range(1, n+1):
    r = []
    for i in range(1, n+1):
        if deg[i] == 1:
            r += [i]
            deg[i] = 0
    if not r:
        break
    ans += 1
    for i in range(1, n+1):
        if deg[i] >= 2:
            for j in r:
                if j in g[i]:
                    deg[i] -= 1
print(ans)