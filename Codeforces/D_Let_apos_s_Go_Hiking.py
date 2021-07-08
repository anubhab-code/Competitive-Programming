n = int(input())
l = [0]+list(map(int, input().split()))+[0]
left = [0]*(n+3)
right = [0]*(n+3)

for i in range(2,n+1):
    if l[i-1] < l[i]:
        left[i] = left[i-1]+1
for i in range(n-1,0,-1):
    if l[i+1] < l[i]:
        right[i] = right[i+1]+1

ll = [0]*(n+3)
rl = [0]*(n+3)

for i in range(1,n+1):
    ll[i] = max(ll[i-1],left[i],right[i])
for i in range(n,0,-1):
    rl[i] = max(rl[i+1],right[i],left[i])

ans = 0
for i in range(1,n+1):
    mx = max(left[i],right[i])
    if max(ll[i-left[i]-1], rl[i+right[i]-1]) < mx:
        if l[i] > l[i-1] and l[i] > l[i+1]:
            if left[i]==right[i] and left[i]%2==0:
                ans += 1
print(ans)