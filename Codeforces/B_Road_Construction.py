n,m = map(int,input().split())
s = set()
for i in range(m):
    u,v = map(int,input().split())
    s.add(u)
    s.add(v)
val=0
for i in range(1,n+1):
    if i not in s:
        val = i
        break
print(n-1)
for j in range(1,n+1):
    if j != val:
        print(val,j)