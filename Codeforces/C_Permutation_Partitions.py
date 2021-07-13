n,k=map(int,input().split())
arr=list(map(int,input().split()))
p=sorted(arr)
d={}
ans1=0
for i in range(n-1,n-k-1,-1):
    d[p[i]]=1
    ans1+=p[i]
cx=0
found=False
ans2=1
for i in range(n):
    if arr[i] in d and not found:
        cx=i
        found=True
        continue
    elif arr[i] in d:
        ans2*=(i-cx)
        ans2%=998244353
        cx=i
print(ans1,ans2%998244353)