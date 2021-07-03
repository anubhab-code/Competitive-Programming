n = int(input())
l = list(map(int,input().split()))
info = 0
num = 0
ans = -1
while num != n:
    ans += 1
    for i in range(n):
        if l[i]>=0 and l[i]<=info:
            l[i] = -1
            info += 1
            num += 1
    l=l[::-1]
print(ans)