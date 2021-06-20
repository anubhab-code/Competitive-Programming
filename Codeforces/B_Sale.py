n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s=0
for i in range(k):
    if arr[i]>0:
        break
    s+=arr[i]
print(abs(s))