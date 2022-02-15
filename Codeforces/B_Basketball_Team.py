def nck(n, k):
    if n<k:
        return 0
    nu = 1
    d = 1
    if k>n-k:
        k = n-k
    for i in range(k):
        nu *= (n - i)
        d *= (i + 1)
    return nu//d

l = input().split()
n = int(l[0])
m = int(l[1])
h = int(l[2])
s = [int(i) for i in input().split()]
total = sum(s)
if total<n:
    print(-1)
else:
    print(1-(nck(total-s[h-1], n-1)/nck(total-1, n-1)))