m = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = [0]*len(a)
d = {}
for i in range(len(b)):
    x = b[i]
    if x in d:
        e = d[x]
        e.append(i)
        d[x] = e

    else:
        d[x] = [i]
a.sort(reverse = True)
b.sort()
for i in range(len(b)):
    x = b[i]
    y = a[i]
    r = d[x]
    j = r.pop()
    d[x] = r
    l[j] = y
print(*l)