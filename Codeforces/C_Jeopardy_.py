n, m = map(int, input().split())
l = list(map(int, input().split()))
mm = list(map(int, input().split()))
ans = 0
a = []
for i in range(n):
    if i+1 not in mm:
        ans+=l[i]
for i in range(0, m):
    v = l[mm[i]-1]
    a.append(v)
a = sorted(a)[::-1]
for i in a:
    if ans >= i:
        ans+=ans
    else:
        ans+=i
print(ans)