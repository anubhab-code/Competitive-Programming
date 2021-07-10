a,b,c = map(int,input().split())
ans = -1
for i in range(10**6):
    a *= 10
    if a//b == c:
        ans = i+1
        break
    a %= b
print(ans)