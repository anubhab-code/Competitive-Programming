n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
x = n//k
for i in range(k):
    c = 0
    for j in range(i,n,k):
        if l[j]==1:
            c += 1
    ans += min(c,x-c)
print(ans)