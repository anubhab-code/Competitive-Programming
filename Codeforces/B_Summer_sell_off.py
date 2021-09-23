n,f = map(int,input().split())
a = [0]*n
ans = 0
for i in range(n):
    k,l = map(int,input().split())
    a[i] = min(2*k,l)-min(k,l)
    ans += min(k,l)
a = sorted(a)
a = a[n-f:]
ans += sum(a)
print(ans)