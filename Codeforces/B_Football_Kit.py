from collections import Counter
n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
home = Counter(x)
away = Counter(y)
ans = 0
mHome, mAway = [n-1]*n, [n-1]*n
for i in range(n):
    if y[i] in home:
        mHome[i] += home[y[i]]
        mAway[i] -= home[y[i]]
for j in range(n):
    print(mHome[j], mAway[j])