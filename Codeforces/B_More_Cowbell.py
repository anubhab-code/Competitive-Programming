n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = []
ans.append(l[-1])
for i in range(n-k):
    ans.append(l[i]+l[(2*(n-k)-i)-1])
print(max(ans))