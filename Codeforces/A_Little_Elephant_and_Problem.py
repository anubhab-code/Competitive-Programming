n = int(input())
l = list(map(int,input().split()))
temp = sorted(l)
c = 0
for i in range(n):
    if l[i] != temp[i]:
        c += 1
if c>2:
    print("NO")
else:
    print("YES")