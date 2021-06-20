n,m = map(int, input().split())
a = list(map(int, input().split()))
b = a.copy()
z = 0
x = 0
for i in range(n):
    a.sort()
    b.sort()
    z += a[0]
    if a[0] == 1:
        a[0] = 1000
    else:
        a[0] -= 1
    x += b[m-1]
    b[m-1] -= 1
print(x,z)