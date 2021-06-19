f = lambda: map(int, input().split())
n, m, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

i, j, c = 0, 0, 0

while i < n and j < m:
    if a[i] + k < b[j]: 
        i += 1
    elif a[i] - k > b[j]: 
        j += 1
    else: 
        i += 1
        j += 1 
        c += 1
print(c)