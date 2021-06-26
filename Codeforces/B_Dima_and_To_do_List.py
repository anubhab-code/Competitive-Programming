n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = []
for i in range(k):
    f = i
    res = 0
    for j in range(i,i+n,k):
        res += l[j]
    ans.append([f,res])
ans = sorted(ans, key=lambda x:x[1])
final = ans[0][0]
print(final+1)