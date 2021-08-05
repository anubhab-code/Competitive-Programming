n, k = map(int, input().split())
a = list(sorted(map(int, input().split()), reverse=True))
s = set()
for i in range(len(a)):
    if a[i] * k not in s:
        s.add(a[i])
print(len(s))