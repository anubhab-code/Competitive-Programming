n = int(input())
l = list(map(int,input().split()))
s = {0}
pre,ans = 0,0
for i in range(n):
    pre+=l[i]
    if pre in s:
        ans+=1
        s = {0}
        pre = l[i]
    s.add(pre)
print(ans)