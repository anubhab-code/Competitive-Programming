n = int(input())
a = list(map(int, input().split()))
ans = a[0]
energy = 0
for i in range(1, n):
    if a[i-1]==a[i]:
        continue
    else:
        energy += a[i-1]-a[i]
        if energy<0:
            ans += abs(energy)
            energy = 0
print(ans)