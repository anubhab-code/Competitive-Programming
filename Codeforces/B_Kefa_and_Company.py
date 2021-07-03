n, d = map(int,input().split())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
l=sorted(l)
i, j, ans, s = 0, 0, 0, 0
while j<n:
    if l[i][0]+d > l[j][0]:
        s+=l[j][1]
        j+=1
    else:
        s-=l[i][1]
        i+=1
    ans=max(ans,s)
print(ans)