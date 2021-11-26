n,s = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l)
m = l[n//2]
ans = 0
for i in range(n//2):
    if l[i]>s:
        ans+=l[i]-s
    if l[n-i-1]<s:
        ans+=s-l[n-i-1]
# print(m)
print(ans+abs(s-m))