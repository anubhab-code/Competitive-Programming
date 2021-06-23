n = int(input())
l = list(map(int, input().split()))
t = l.copy()
t.sort()
s1 = [0]
for i in range(n):
    s1.append(s1[-1] + l[i])
s2 = [0]
for i in range(n):
    s2.append(s2[-1] + t[i])
for _ in range(int(input())):
    r, a, b = map(int, input().split())
    if r == 1:
        ans = s1[b] - s1[a-1]
        print(ans)
    else:
        ans = s2[b] - s2[a-1]
        print(ans)