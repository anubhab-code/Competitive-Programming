n = int(input())
l = list(map(int, input().split()))
l=sorted(l)
c = 1
ans = 0
for i in l:
    ans += abs(i-c)
    c += 1
print(ans)
