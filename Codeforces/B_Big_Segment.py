l=[]
r=[]
for _ in range(int(input())):
    t = list(map(int,input().split()))
    l.append(t[0])
    r.append(t[1])
c=(min(l),max(r))
m=zip(l,r)
flag=0
ans=1
for i in m:
    if i==c:
        flag=1
        break
    else:
        ans+=1
if flag==0:
    print(-1)
else:
    print(ans)