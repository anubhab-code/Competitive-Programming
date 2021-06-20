n = int(input())
a = list(map(int, input().split()))
ss = sum(a)
a.sort()
if ss%2 == 1:
    for i in range(0, n):
        if a[i]%2 == 1:
            ss -= a[i]
            break
print(ss)