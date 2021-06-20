l=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    l.append([a,b])
c,ans=0,0
for i in range(0,len(l)):
    c-=l[i][0]
    c+=l[i][1]
    if c>ans:
        ans=c
print(ans)