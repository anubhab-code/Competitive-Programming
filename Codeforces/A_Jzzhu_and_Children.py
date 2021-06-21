import math
n,m = map(int,input().split())
l = list(map(int,input().split()))
for i in range(n):
    l[i] = math.ceil(l[i]/m)
index = n-1
for i in range(n-1, -1, -1):
    if l[i] > l[index]:
        index = i
print(index + 1)