n = int(input())
l = list(map(int,input().split()))
s = sum(l)
ans = -1
c = 0
for i in l:
    if i == 1:
        c -= 1
    else:
        c += 1
    ans = max(c, ans)
    if c < 0:
        c = 0
print(ans+s)


