n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in l:
    temp = l.count(i)
    ans = max(temp,ans)
print(n-ans)