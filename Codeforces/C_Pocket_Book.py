mod=10**9+7
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
ans=1
for j in range(m):
    s=set()
    for i in range(n):
        s.add(l[i][j])
    ans=(ans*len(s))%mod
print(ans%mod)