n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
s = sum(l)
a = s/n
while a<k-0.5:
    s += k
    ans += 1
    a = s/(n+ans)
print(ans)