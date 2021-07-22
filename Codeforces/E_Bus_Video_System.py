n,w = map(int,input().split())
a = list(map(int,input().split()))
mx=0
mn=0
s=0
for i in range(n):
    s+=a[i]
    mx=max(mx,s)
    mn=min(mn,s)
print(max(w-(mx-mn)+1,0))