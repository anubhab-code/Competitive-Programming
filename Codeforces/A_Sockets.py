n, m, k = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
ans = 0
if k < m:
    spots = k
    end = n-1
    while spots < m and end >= 0:
        spots += f[end]-1
        ans += 1
        end -= 1
    if spots<m:
        print(-1)
    else:
        print(ans)
else:
    print(0)