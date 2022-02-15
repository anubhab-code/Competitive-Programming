n,t = map(int,input().split())
l = list(map(int,input().split()))
i = 0
k = l[0]
ans = (l[0])*(t//k) + t%k
while i<n:
    for j in range(i+1,n):
        ans = max(ans,(l[j])*(t//k) + t%k)
    i+=1
    if i<n:
        k = l[i]
print(ans)