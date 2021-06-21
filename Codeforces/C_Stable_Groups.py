n,k,x = list(map(int,input().split()))
l = list(map(int,input().split()))
l=sorted(l)
ans = []
for i in range(n):
    if l[i]-l[i-1]>x:
        ans.append((l[i]-l[i-1]-1)//x)
ans = sorted(ans)[::-1]
t = len(ans)
while t:
    if ans[t-1] <= k:
        k-=ans[t-1]
        t-=1
    else:
        break
final=t+1
print(final)