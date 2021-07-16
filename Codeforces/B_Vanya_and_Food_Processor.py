from math import ceil
n,h,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
for i in range(n):
    if i < n-1:
        ans += arr[i]//k
        if arr[i]%k + arr[i+1] <= h:
            arr[i+1] += arr[i]%k
        else:
            ans += 1
    if i == n-1:
        ans += ceil(arr[i]/k)
print(ans)